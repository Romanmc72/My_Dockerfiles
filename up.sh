#!/usr/bin/env bash

# shortcut for launching docker-compose.
# Lives at the root here and can be
# symlinked to the other directories
# for ease of use
PORT=$1

set -euxo pipefail

browser_url="http://localhost:${PORT}"

docker-compose up -d --build
docker ps
open $browser_url || echo 'could not open localhost'
