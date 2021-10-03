#!/usr/bin/env bash

set -euo pipefail

source ./version.env

main() {
    # Ensure that you are signed into ECR from docker to be able to push
    local build_env="$1"
    local cmd=""
    local local_cmd="docker build -t romanmc72/fake-data-api:${tag} -f Dockerfile . && docker push romanmc72/fake-data-api:${tag}"
    local aws_cmd="docker build -t 005071865344.dkr.ecr.us-east-1.amazonaws.com/r0m4n.com/fake-data-api:${tag} -f Dockerfile.aws.lambda . && docker push 005071865344.dkr.ecr.us-east-1.amazonaws.com/r0m4n.com/fake-data-api:${tag}"
    case $build_env in
        "local" | "l" )
            cmd=$local_cmd
            ;;
        "aws" | "a" )
            cmd=$aws_cmd
            ;;
        "both" | "b" )
            cmd="${local_cmd} && ${aws_cmd}"
            ;;
        * )
            echo "To build the images, provide the env to build in and the tag"
            echo "to tag tht image with (image will be pushed after build succeeds)."
            echo "Args:"
            echo "    - \$1 'env' (l|local|a|aws|b|both) "
            echo "    - \$2 'tag' e.g. '0.0.1'"
            return 1
            ;;
    esac
    eval $cmd
}

main $@
