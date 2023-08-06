#!/usr/bin/env bash

set -e

source $(dirname $0)/enough-lxc-helpers-test.sh

export TMPDIR=/opt
TMP_DIR=$(mktemp -d)

function cleanup_tmp() {
    rm -fr ${TMP_DIR}
    TMP_DIR=$(mktemp -d)
}

function teardown() {
    for f in $(set | sed -n -e 's/^\([0-9a-z_]*_teardown\) .*/\1/p'); do
	$f || true
    done
    cleanup_tmp
}

function setup() {
    test_activate_trace
    for f in $(set | sed -n -e 's/^\([0-9a-z_]*_setup\) .*/\1/p'); do
	$f || true
    done
}

function test_activate_trace() {
    set -x
    PS4='${BASH_SOURCE[0]}:$LINENO: ${FUNCNAME[0]}:  '
}

function test_deactivate_trace() {
    unset PS4
    set +x
}

trap "test_deactivate_trace ; teardown" EXIT

teardown
setup

function run() {
    for t in "$@"; do
	echo "===================== TEST $t BEGINS ====================="
	$t
	echo "===================== TEST $t ENDS ====================="
    done
}
    
run "$@"
