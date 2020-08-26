#!/usr/bin/env bash

# shortcut for launching docker-compose.
# Lives at the root here and can be
# symlinked to the other directories
# for ease of use

set -euxo pipefail

docker-compose up -d --build
docker ps
open http://localhost:5000
