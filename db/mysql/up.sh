#!/usr/bin/env bash

set -euxo pipefail

docker-compose up -d 
docker ps
open http://localhost:8080
