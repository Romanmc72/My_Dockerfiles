#!/usr/bin/env bash

set -euo pipefail

main() {
    export MINECRAFT_SERVER_DATA=$HOME/minecraft/minecraft_server_data
    docker-compose up -d
}

main
