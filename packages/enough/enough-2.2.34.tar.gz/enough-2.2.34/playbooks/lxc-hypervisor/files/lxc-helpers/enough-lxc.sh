#!/usr/bin/env bash

set -e

source $(dirname $0)/enough-lxc-helpers.sh

function main() {
    echo help
}

${@:-main}
