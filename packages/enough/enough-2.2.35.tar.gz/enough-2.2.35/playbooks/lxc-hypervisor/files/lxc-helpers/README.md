# LXC helpers

A set of [LXC](https://linuxcontainers.org/lxc/) shell functions to help with:

* Isolating runs in a CI (see https://code.forgejo.org/forgejo/act for an example)
* Managing system containers with Ansible (see https://lab.enough.community/main/infrastructure for an example)
* Running CI jobs that need nested system containers (see https://code.forgejo.org/actions/setup-forgejo for an example)

# Usage

```shell
$ lxc-helpers.sh --help
lxc-helpers.sh - LXC container management helpers

SYNOPSIS

   lxc-helpers.sh [-v|--verbose] [-h|--help]
		  [-o|--os {bookworm|bullseye} (default bookworm)]
		  command [arguments]

DESCRIPTION

   A thin shell based layer on top of LXC to create, populate, run and
   destroy LXC containers. A container is created from a copy of an
   existing container.

CREATE AND DESTROY

   lxc_prepare_environment

       Install LXC dependencies.

   lxc_template_release

       Echo the name of the container for the Operating System
       specified with `--os`.

   lxc_build_template `existing_container` `new_container`

       Copy `existing_container` into `new_container`. If
       `existing_container` is equal to $(lxc-helpers.sh lxc_template_release) it
       will be created on demand.

   lxc_container_mount `name` `path`

       Configure `name` container to bind mount `path` so that it is
       also accessible at `path` from within the container.

   lxc_container_start `name`

       Start the `name` container.

   lxc_container_stop `name`

       Stop the `name` container.

   lxc_container_destroy `name`

       Call lxc_container_stop `name` and destroy the container.

ACTIONS IN THE CONTAINER

   For some command lxc_something `name` that can be called from outside the container
   there is an equivalent function lxc_something_inside that can be called from inside
   the container.

   lxc_install_lxc `name` `prefix`
   lxc_install_lxc_inside `prefix`

      Install LXC in the `name` container to allow the creation of
      named containers. `prefix` is a class C IP prefix from which
      containers will obtain their IP (for instance 10.40.50).

   lxc_container_run_script `name` `path`
   lxc_container_run_script_as `name` `user` `path`

      Run the script found at `path` within the `name` container. The
      environment is cleared before running the script. The first form
      will run as root, the second form will impersonate `user`.

   lxc_container_user_install `name` `user_id` `user` [`homedir` default `/home`]

      Create the `user` with `user_id` in the `name` container with a
      HOME at `/homedir/user`. Passwordless sudo permissions are
      granted to `user`. It is made a member of the groups docker, kvm
      and libvirt if they exist already. A SSH key is created.

      Example: lxc_container_user_install mycontainer $(id -u) $(USER)
