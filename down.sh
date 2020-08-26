#!/usr/bin/env bash

# shortcut for stopping docker-compose.
# Lives at the root here and can be
# symlinked to the other directories
# for ease of use

set -euxo pipefail

docker ps
docker-compose down --remove-orphans
docker ps
