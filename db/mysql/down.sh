#!/usr/bin/env bash

set -euxo pipefail

docker ps
docker-compose down --remove-orphans
docker ps
