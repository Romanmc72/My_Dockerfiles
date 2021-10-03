#!/usr/bin/env bash

set -euo pipefail

main() {
    case "$#" in
        "1" )
            local tag="$1"
            ;;
        * )
            local tag="0.0.1"
            echo "defaulting to ${tag}, none specified."
            ;;
    esac
        # --rm \
    docker run \
        -d \
        -p 8000:8000 \
        --name fake-data-api \
        "romanmc72/fake-data-api:${tag}"
}

main $@
