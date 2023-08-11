#!/usr/bin/env bash

set -euxo pipefail

mkdir -p ./.monero
docker-compose up -d --build
docker ps

