#!/bin/bash

set -e

source $(dirname $0)/files/lxc-helpers/enough-lxc-helpers.sh

function run_playbook() {
    local name="enough-test-playbook-lxc"

    lxc_prepare_environment
    lxc_build_template $(lxc_template_release) $name
    lxc_container_start $name
    lxc_container_user_install $name 1000 debian
    sudo cp ~/.ssh/id_rsa.pub $(lxc_root $name)/home/debian/.ssh/authorized_keys
    local ip=$($LXC_SUDO lxc-info --no-humanize --ips $name | head -1)
    local inventory=$(mktemp -d)
    tee $inventory/hosts.yml <<EOF
live:
  hosts:
    lxc-hypervisor:
      ansible_host: $ip
      ansible_user: debian
EOF
    ssh-keyscan $ip >& ~/.ssh/known_hosts
    ansible-playbook --extra-vars lxc_prefix=10.88.0 --private-key ~/.ssh/id_rsa -i $inventory playbooks/lxc-hypervisor/lxc-playbook.yml
    lxc_container_destroy $name
}

run_playbook
