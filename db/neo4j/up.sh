#!/usr/bin/env bash
local localport=7474

echo 'Starting Neo4j...'
docker run \
    -d \
    --rm \
    --publish=$localport:7474 \
    --publish=7687:7687 \
    --volume=./data:/data \
    --env=NEO4J_AUTH=none \
    neo4j:4.1.1

docker ps

echo 'Opening browser...'
open http://localhost:$localport

echo 'Enjoy!'
