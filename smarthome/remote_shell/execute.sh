#!/usr/bin/env bash

set -euo pipefail

source secrets.env

cmd=$1
image_name="romanmc72/remote_shell"
image_tag="0.0.1"
image_ref="${image_name}:${image_tag}"

function build_image() {
    docker build images/ -t $image_ref
}
function run_container() {
    docker run \
        --rm \
        -it \
        -e USERNAME=$USERNAME \
        -e HOSTNAME=$HOSTNAME \
        -e PASSWORD=$PASSWORD \
        $image_ref \
        --cmd="${cmd}"
}

function main() {
    build_image
    run_container
}

main
