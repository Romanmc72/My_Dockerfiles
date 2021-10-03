#!/usr/bin/env bash

set -euo pipefail

main() {
    docker stop fake-data-api
}

main $@
