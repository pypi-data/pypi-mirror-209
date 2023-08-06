#!/usr/bin/env python3

import argparse
import logging
import requests
import sh
import shutil
import sys
import tempfile
import time
from furl import furl
from dataclasses import dataclass
from functools import wraps

logging.basicConfig()
logger = logging.getLogger(__name__)


class RetryException(Exception):
    pass


def retry(exceptions, tries=2, delay=1):
    def deco_retry(f):
        @wraps(f)
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries + 1, delay
            while mtries > 0:
                try:
                    return f(*args, **kwargs)
                except exceptions as e:
                    logger.info('%s: %s, Retrying in %s seconds...', f.__qualname__, e, mdelay)
                    if mtries == tries + 1:
                        logger.debug("", exc_info=True)
                    time.sleep(mdelay)
                    mtries -= 1
                    mdelay *= 2
            raise RetryException("Number of retries exceeded for function " + f.__name__)
        return f_retry
    return deco_retry


class Forgejo(object):
    def __init__(self, hostname):
        self._hostname = hostname
        self._url = f'https://{hostname}'
        self._users = self.users_factory()(self)
        self._projects = self.projects_factory()(self)
        self._s = requests.Session()

    @property
    def hostname(self):
        return self._hostname

    @property
    def url(self):
        return self._url

    @property
    def projects(self):
        return self._projects

    @property
    def users(self):
        return self._users

    @property
    def s(self):
        return self._s

    def certs(self, certs):
        self.s.verify = certs
        return self

    def authenticate(self, **kwargs):
        self._session()
        self.login(kwargs["username"], kwargs["password"], kwargs["scopes"])
        self._user = self.s.get(f"{self.s.api}/user").json()

    @property
    def is_authenticated(self):
        return hasattr(self, "_user")

    @property
    def username(self):
        return self._user["login"]

    @property
    def is_admin(self):
        return self._user["is_admin"]

    def _session(self):
        self.s.api = f"{self.url}/api/v1"

    def login(self, username, password, scopes):
        self.password = password
        r = self.s.post(
            f"{self.s.api}/users/{username}/tokens",
            auth=(username, password),
            json={
                "name": f"TEST{time.time()}",
                "scopes": scopes,
            },
        )
        r.raise_for_status()
        self.set_token(r.json())

    def logout(self):
        self.delete_token()
        if self.is_authenticated:
            del self._user

    def set_token(self, token):
        self.token = token
        self.s.headers["Authorization"] = f"token {self.token['sha1']}"

    def get_token(self):
        return self.token['sha1']

    def delete_token(self):
        if hasattr(self, 'token'):
            r = self.s.delete(
                f"{self.s.api}/users/{self.username}/tokens/{self.token['id']}",
                auth=(self.username, self.password),
            )
            r.raise_for_status()
            del self.token
            return True
        else:
            return False

    def projects_factory(self):
        return ForgejoProjects

    def users_factory(self):
        return ForgejoUsers


class ForgejoUsers(object):
    def __init__(self, forge):
        self._forge = forge

    @property
    def forge(self):
        return self._forge

    @property
    def s(self):
        return self.forge.s

    def get(self, username):
        if username == self.forge.username:
            r = self.s.get(f"{self.s.api}/user")
        elif self.forge.is_admin:
            r = self.s.get(f"{self.s.api}/user", params={"sudo": username})
        else:
            r = self.s.get(f"{self.s.api}/users/{username}")
        if r.status_code == 404:
            return None
        else:
            r.raise_for_status()
            return ForgejoUser(self.forge, r.json())

    def delete(self, username):
        user = self.get(username)
        if user is None:
            return False
        while True:
            r = self.s.delete(f"{self.s.api}/admin/users/{username}")
            if r.status_code == 404:
                break
            if r.status_code != 204:
                logger.error(f"{r.status_code}: {r.text}")
            logger.debug(r.text)
            r.raise_for_status()
        return True

    def create(self, username, password, email, **data):
        # the API does not support creating an admin user
        assert data.get("admin") is not True, "Creating admin user with Forgejo is not implemented"
        info = self.get(username)
        if info is None:
            r = self.s.post(
                f"{self.s.api}/admin/users",
                data={
                    "username": username,
                    "email": email,
                    "password": password,
                },
            )
            if r.status_code != 201:
                logger.error(r.text)
            r.raise_for_status()
            info = r.json()
            Forgejo(self.forge.hostname).certs(self.s.verify).users._finalize_user_create(
                username, password)
            info = self.get(username)
        return info

    def _finalize_user_create(self, username, password):
        r = self.s.post(
            f"{self.forge.url}/user/login",
            data={
                "user_name": username,
                "password": password,
            },
        )
        r.raise_for_status()
        r = self.s.post(
            f"{self.forge.url}/user/settings/change_password",
            data={
                "password": password,
                "retype": password,
                "_csrf": self.s.cookies["_csrf"],
            },
        )
        r.raise_for_status()

    def list(self):
        r = self.s.get(f"{self.s.api}/users/search")
        r.raise_for_status()
        j = r.json()
        assert j["ok"]
        for u in j["data"]:
            yield ForgejoUser(self.forge, u)


class ForgejoUser(object):
    def __init__(self, forge, user):
        self._forge = forge
        self._user = user

    @property
    def url(self):
        return f"{self.forge.url}/{self.username}"

    @property
    def username(self):
        return self._user["username"]

    @property
    def forge(self):
        return self._forge

    @property
    def s(self):
        return self.forge.s

    def __eq__(self, other):
        return (
            isinstance(other, ForgejoUser)
            and self.forge == other.forge
            and self.url == other.url
            and self.username == other.username
        )

    def get_keys(self):
        r = self.s.get(f"{self.s.api}/user/keys")
        r.raise_for_status()
        return r.json()

    def get_key(self, title):
        for key in self.get_keys():
            if key["title"] == title:
                return key
        return None

    def delete_key(self, title):
        key = self.get_key(title)
        if key:
            r = self.s.delete(f"{self.s.api}/user/keys/{key['id']}")
            r.raise_for_status()

    def create_key(self, title, key):
        data = {
            "title": title,
            "key": key,
        }
        r = self.s.post(f"{self.s.api}/user/keys", data=data)
        logger.debug(r.text)
        r.raise_for_status()

    def get_applications(self):
        r = self.s.get(f"{self.s.api}/user/applications/oauth2")
        r.raise_for_status()
        return r.json()

    def get_application(self, name):
        for app in self.get_applications():
            if app["name"] == name:
                return app
        return None

    def delete_application(self, name):
        app = self.get_application(name)
        if app:
            r = self.s.delete(f"{self.s.api}/user/applications/oauth2/{app['id']}")
            r.raise_for_status()
        return app

    def create_application(self, name, redirect_uri):
        app = self.get_application(name)
        if app is None:
            data = {
                "name": name,
                "redirect_uris": [redirect_uri],
            }
            r = self.s.post(f"{self.s.api}/user/applications/oauth2", json=data)
            r.raise_for_status()
            app = self.get_application(name)
        return app

    @property
    def projects(self):
        params = {"uid": self._user["id"]}
        projects = self.s.get(f"{self.s.api}/repos/search", params=params)
        projects.raise_for_status()
        raw = projects.json()
        assert raw["ok"]
        for project in raw["data"]:
            yield ForgejoProject(self.forge, project)


class ForgejoProjects(object):
    def __init__(self, forge):
        self._forge = forge

    @property
    def forge(self):
        return self._forge

    @property
    def s(self):
        return self.forge.s

    def project_factory(self):
        return ForgejoProject

    def get(self, namespace, project):
        r = self.s.get(f"{self.s.api}/repos/{namespace}/{project}")
        if r.status_code == requests.codes.ok:
            return self.project_factory()(self.forge, r.json())
        else:
            return None

    class DeletionInProgress(Exception):
        pass

    @retry(DeletionInProgress, tries=5)
    def _create(self, namespace, project, **data):
        data.update(
            {
                "name": project,
            }
        )
        r = self.s.post(f"{self.s.api}/user/repos", data=data)
        logger.debug(r.text)
        if r.status_code == 201:
            return self.get(namespace, project)
        r.raise_for_status()

    def create(self, namespace, project, **data):
        p = self.get(namespace, project)
        if p is None:
            return self._create(namespace, project, **data)
        else:
            return p

    def delete(self, namespace, project):
        p = self.get(namespace, project)
        if p is None:
            return False
        r = self.s.delete(f"{self.s.api}/repos/{namespace}/{project}")
        r.raise_for_status()
        while self.get(namespace, project) is not None:
            time.sleep(1)
        return True

    def list(self):
        projects = self.s.get(f"{self.s.api}/repos/search")
        projects.raise_for_status()
        raw = projects.json()
        assert raw["ok"]
        for project in raw["data"]:
            yield ForgejoProject(self.forge, project)


class ForgejoProject(object):
    def __init__(self, forge, project):
        self._forge = forge
        self._project = project
        self._keys = ForgejoProjectKeys(self)

    @property
    def forge(self):
        return self._forge

    @property
    def s(self):
        return self.forge.s

    @property
    def id(self):
        return self._project["id"]

    @property
    def namespace(self):
        return self._project["owner"]["login"]

    @property
    def project(self):
        return self._project["name"]

    @property
    def keys(self):
        return self._keys

    @property
    def ssh_url_to_repo(self):
        return self._project["ssh_url"]

    @property
    def http_url_to_repo(self):
        return self._project["clone_url"]

    @property
    def http_url_to_repo_with_auth(self):
        o = furl(self.http_url_to_repo)
        o.username = self.forge.username
        o.password = self.forge.get_token()
        return o.tostr()

    def get_applications(self):
        r = self.s.get(f"{self.s.api}/user/applications/oauth2")
        r.raise_for_status()
        return r.json()

    def get_status(self, sha):
        r = self.s.get(
            f"{self.s.api}/repos/{self.namespace}/{self.project}/commits/{sha}/status")
        if r.status_code == 500:
            return {}
        r.raise_for_status()
        return r.json()

    def __eq__(self, other):
        return (
            isinstance(other, ForgejoProject)
            and self.id == other.id
            and self.namespace == other.namespace
            and self.project == other.project
            and self.http_url_to_repo == other.http_url_to_repo
            and self.ssh_url_to_repo == other.ssh_url_to_repo
        )


class ForgejoProjectKeys(object):
    def __init__(self, project):
        self._project = project

    @property
    def project(self):
        return self._project

    @property
    def s(self):
        return self.project.s

    def _build_url(self):
        return f"{self.s.api}/repos/{self.project.namespace}/{self.project.project}/keys"

    def get(self, id):
        response = self.s.get(f"{self._build_url()}/{int(id)}")  # ensure id is not None
        if response.status_code == 404:
            return None
        else:
            response.raise_for_status()
            return ForgejoProjectKey(self.project, response.json())

    def delete(self, id):
        p = self.get(id)
        if p is None:
            return False
        r = self.s.delete(f"{self._build_url()}/{id}")
        r.raise_for_status()
        return True

    def _create(self, title, key, read_only):
        data = {
            "title": title,
            "key": key,
            "read_only": read_only,
        }
        response = self.s.post(f"{self._build_url()}", data=data)
        logger.info(response.text)
        if response.status_code == 201:
            key = response.json()
            return self.get(key["id"])
        response.raise_for_status()

    def create(self, title, key, read_only):
        for k in self.list():
            if k.key == key:
                return k
        return self._create(title, key, read_only)

    def list(self):
        response = self.s.get(f"{self._build_url()}")
        response.raise_for_status()
        for key in response.json():
            yield ForgejoProjectKey(self.project, key)


class ForgejoProjectKey(object):
    def __init__(self, project, key):
        self._project = project
        self._key = key

    @property
    def project(self):
        return self._project

    @property
    def id(self):
        return self._key["id"]

    @property
    def key(self):
        return self._key["key"]

    @property
    def title(self):
        return self._key["title"]

    def __eq__(self, other):
        return (
            isinstance(other, ForgejoProjectKey)
            and self.id == other.id
            and self.title == other.title
        )


@dataclass
class Hostea(object):
    certs: str
    forgejo_hostname: str
    admin_user: str
    admin_password: str
    user: str
    password: str
    email: str
    project: str
    deploy: str = None
    verbose: bool = False
    debug: bool = False

    def setup(self):
        self.forgejo_create()
        self.forgejo_user_create()
        self.forgejo_project_create()
        self.forgejo_add_deploy()

    def destroy(self):
        self.forgejo_create()
        self.forgejo.authenticate(
            username=self.admin_user, password=self.admin_password, scopes=['all', 'sudo'])
        if self.forgejo.users.get(self.user):
            self.destroy_project()
            self.forgejo.users.delete(self.user)
        self.forgejo.logout()

    def update_project(self, content_dir):
        self.git_init_project()
        self.git_checkout_project()
        shutil.copytree(content_dir, self.git_directory.name, dirs_exist_ok=True)
        return self.git_push_project()

    def git_push_project(self):
        self.git.add('.')
        self.git.config('user.email', self.email)
        self.git.config('user.name', self.user)
        try:
            self.git.commit('-m', 'hostea: hosteasetup.py update complete')
        except sh.ErrorReturnCode_1:
            logger.debug("no change")
        else:
            self.git.push('origin', 'master')
        sha = self.git('rev-parse', 'origin/master')
        return str(sha).strip()

    def git_checkout_project(self):
        try:
            self.git('ls-remote', '--quiet', '--exit-code', 'origin', 'master')
            self.git.checkout('-b', 'master', 'origin/master')
        except sh.ErrorReturnCode_2:
            logger.debug("repository is empty")

    def git_init_project(self):
        if hasattr(self, 'git'):
            return False
        self.git_directory = tempfile.TemporaryDirectory()
        self.git = sh.git.bake(_cwd=self.git_directory.name)
        self.git.init()

        p = self.forgejo.projects.get(self.user, self.project)
        url = p.http_url_to_repo_with_auth
        self.git.config('http.sslVerify', 'false')
        self.git.remote.add.origin(url)
        self.git.fetch()
        return True

    def destroy_project(self):
        self.forgejo.projects.delete(self.user, self.project)

    def forgejo_create(self):
        self.forgejo = Forgejo(self.forgejo_hostname)
        self.forgejo.certs(self.certs)

    def forgejo_user_create(self):
        self.forgejo.authenticate(
            username=self.admin_user, password=self.admin_password, scopes=['all', 'sudo'])
        self.forgejo.users.create(self.user, self.password, self.email)
        self.forgejo.authenticate(username=self.user, password=self.password, scopes=['all'])

    def forgejo_project_create(self):
        return self.forgejo.projects.create(self.user, self.project, private=False)

    def forgejo_add_deploy(self):
        return self.forgejo.projects.get(self.user, self.project).keys.create(
            title="deploy",
            key=open(f"{self.deploy}.pub").read().strip(),
            read_only=False)

    def forgejo_wait_status(self, sha):
        project = self.forgejo.projects.get(self.user, self.project)

        @retry(AssertionError, tries=60)
        def wait_status():
            state = project.get_status(sha).get("state")
            assert state not in ("pending", "running", None)
            return state
        return wait_status()


def main(argv):
    parser = argparse.ArgumentParser(description='Hostea setup.')
    parser.add_argument('--deploy', help='path to the private deploy key')
    parser.add_argument('--certs', help='directory with certificate authorities')
    parser.add_argument('--verbose', action='store_true', help='verbose output')
    parser.add_argument('--debug', action='store_true', help='debug output')
    parser.add_argument(
        '--update-directory',
        help='update the project repository with the content of this directory')
    parser.add_argument('forgejo_hostname')
    parser.add_argument('admin_user')
    parser.add_argument('admin_password')
    parser.add_argument('user')
    parser.add_argument('password')
    parser.add_argument('email')
    parser.add_argument('project')
    args = parser.parse_args(argv)

    if args.debug:
        logger.setLevel(logging.DEBUG)
    elif args.verbose:
        logger.setLevel(logging.INFO)

    d = vars(args)
    update_directory = d['update_directory']
    del d['update_directory']
    hostea = Hostea(**d)
    hostea.setup()
    if update_directory:
        hostea.update_project(update_directory)
    return hostea.forgejo


if __name__ == '__main__':
    main(sys.argv[1:])
