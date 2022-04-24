#!/usr/bin/env bash

set -euo pipefail

source ./secrets.env

main() {
    if [ -z "$(docker ps | grep postgres)" ]
    then
        launch_postgres_stack;
    else
        echo 'Postgres already running';
    fi
    docker run \
        -d \
        --rm \
        -e ITERATIONS_TO_RUN='-1' \
        -e SLEEP_INTERVAL=$SLEEP_INTERVAL \
        -e IP_TO_PING='r0m4n.com' \
        -e POSTGRES_HOST=$POSTGRES_HOST \
        --network postgres_default \
        romanmc72/is_it_down:latest
}

launch_postgres_stack() {
    pushd ../../../My_Dockerfiles/db/postgres/
    ./up.sh
    popd
}

main
