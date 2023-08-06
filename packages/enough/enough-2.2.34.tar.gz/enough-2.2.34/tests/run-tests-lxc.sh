#!/bin/bash

set -e

source $(dirname $0)/../playbooks/lxc-hypervisor/files/lxc-helpers/enough-lxc-helpers.sh

export LXC_CONTAINER_RELEASE=bullseye
export LXC_HOME=/opt/home

function prepare_repository() {
    git submodule --quiet sync
    git submodule --quiet update --init --recursive
}

function prepare_inventory() {
    if ! test -f tests/clouds.yml ; then
	cat > tests/clouds.yml <<EOF
clouds:
  production:
    auth:
      auth_url: "https://auth.cloud.ovh.net/v3/"
      project_name: "AAAAAAA"
      project_id: "BBBBB"
      user_domain_name: "CCCCCCC"
      username: "DDDDDDD"
      password: "EEEEEEEE"
    region_name: "FFFFFF"
EOF
    fi
    cp -a tests/clouds.yml inventory/group_vars/all/clouds.yml

    if ! test -f inventory/group_vars/all/domain.yml ; then
        cat > tests/domain.yml <<EOF
---
domain: enough.community
EOF
        cp tests/domain.yml inventory/group_vars/all/domain.yml
    else
        cat inventory/group_vars/all/domain.yml > tests/domain.yml
    fi
}

function template_test() {
    echo $(lxc_template_release)-test
}

function build_template_test() {
    local name="$(template_test)"

    if lxc_exists $name ; then
	return
    fi

    lxc_build_template $(lxc_template_release) $name
    lxc_container_start $name
    lxc_install_lxc $name 10.84.28
    lxc_install_docker $name
    # enough
    lxc_apt_install $name curl virtualenv python3 gcc libffi-dev libssl-dev python3-dev make git rsync
    # kvm, libvirt
    lxc_apt_install $name libguestfs-tools linux-image-cloud-amd64 python3-lxml pkg-config python3-libvirt libvirt-dev virtinst libvirt-clients libvirt-daemon-system
    # dependencies of playbooks/hostea/tests/test_hostea.py
    lxc_apt_install $name bind9-dnsutils
    # this is not necessary to run tests but to cleanup leftovers when tests fail
    lxc_apt_install $name python3-openstackclient python3-heatclient python3-glanceclient
    # dependencies of test/ssh
    lxc_apt_install $name jq
    lxc_container_stop $name
}

function build_template() {
    local name="$1"

    if lxc_exists $name ; then
	return
    fi

    build_template_test
    lxc_build_template $(template_test) $name
    lxc_container_start $name
    lxc_container_user_install $name $(id -u) $USER
    container_python_install $name
    lxc_container_stop $name
}

function container_python_install() {
    local name="$1"

    local root=$(lxc_root $name)
    local home=$root/opt/home/$USER
    local home_inside=/opt/home/$USER
    local bin_inside=$home_inside/venv/bin
    local update=false
    local files="requirements.txt requirements-dev.txt tox.ini docs/requirements.txt"
    for f in $files ; do
	if $LXC_SUDO test $f -nt $home/$f ; then
	    update=true
	    break
	fi
    done

    if $update ; then
	if ! $LXC_SUDO grep --quiet $bin_inside $home/.bashrc ; then
	    $LXC_SUDO tee -a $home/.bashrc <<< "export PATH=$bin_inside:$PATH"
	fi
	$LXC_SUDO mkdir -p $home/docs
	for f in $files ; do
	    $LXC_SUDO cp -a $f $home/$f
	done
	$LXC_SUDO tee $home/tox-dry-run.sh <<EOF
#!/bin/bash
cd $home_inside
export PATH=$bin_inside:$PATH
virtualenv --python=python3 venv
pip install -r requirements.txt -r requirements-dev.txt
tox --notest -e py3_cache,flake8,docs
EOF
	lxc_container_run_script_as $name $USER $home_inside/tox-dry-run.sh
    fi
}

function container_name() {
    echo enough-tox-$(pwd | md5sum | cut -f1 -d' ')
}

function run_test() {
    local name="$1"
    shift

    local sources=$(git rev-parse --show-toplevel)

    lxc_container_start $name $sources
    local root=$(lxc_root $name)
    local opt=$root/opt
    $LXC_SUDO tee $opt/script.sh > /dev/null <<EOF
#!/bin/bash
cd $sources
export PATH=\$HOME/venv/bin:\$PATH
$@
EOF
    lxc_container_run_script_as $name $USER /opt/script.sh
    lxc_container_stop $name $sources
}

function main() {
    lxc_prepare_environment
    prepare_inventory

    local name=$(container_name)
    build_template $name
    run_test $name "$@"
}

main "$@"
