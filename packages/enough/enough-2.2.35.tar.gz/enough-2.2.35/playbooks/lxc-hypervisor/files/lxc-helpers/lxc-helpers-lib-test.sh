#!/usr/bin/env bash
# SPDX-License-Identifier: MIT

source $(dirname $0)/lxc-helpers-lib.sh

function test_lxc_helpers_teardown() {
    local name=lxc_helper_test

    lxc_container_stop $name
    lxc_container_destroy $name
    lxc_container_destroy $(lxc_template_release)
}

function test_lxc_helpers() {
    local name=lxc_helper_test

    test_lxc_helpers_teardown $name

    lxc_prepare_environment
    lxc_build_template $(lxc_template_release) $name

    lxc_container_mount $name $TMP_DIR
    lxc_container_mount $name $TMP_DIR # do it twice to make sure it is idempotent
    test $($LXC_SUDO grep --count $TMP_DIR $(lxc_config $name)) = 1

    lxc_container_start $name
    touch $TMP_DIR/lxc_helper_test.stone
    lxc_install_lxc $name 10.250.100
    lxc_install_docker $name
    lxc_container_user_install $name 1000 debian

    ( echo '#!/bin/bash' ; echo id ) | $LXC_SUDO tee $(lxc_root $name)/usr/local/bin/script.sh
    lxc_container_run_script_as $name debian /usr/local/bin/script.sh | tee $TMP_DIR/script.output
    grep debian $TMP_DIR/script.output

    $LXC_SUDO lxc-attach --name $name -- docker --version
    $LXC_SUDO lxc-attach --name $name -- systemctl is-active --quiet lxc-net
    $LXC_SUDO lxc-attach --name $name -- sudo id
    $LXC_SUDO lxc-attach --name $name -- test -f $TMP_DIR/lxc_helper_test.stone
    $LXC_SUDO lxc-attach --name $name -- which python3

    test_lxc_helpers_teardown $name
}
