#!/usr/bin/env bash

set -euo pipefail

main() {
    docker-compose down --remove-orphans
}

main
