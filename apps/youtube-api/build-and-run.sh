#!/usr/bin/env bash

set -euo pipefail

main() {
    local image_name="romanmc72/youtube-subscriber-count"
    local image_tag="0.0.1"
    docker build -t "${image_name}:${image_tag}" .
    source app/secrets.env
    docker run --rm -e GOOGLE_API_KEY=$GOOGLE_API_KEY "${image_name}:${image_tag}" $@
}

main $@
