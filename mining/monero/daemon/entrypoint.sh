#!/usr/bin/sh

set -euo pipefail

main() {
    monero-blockchain-import --input-file "$BLOCKCHAIN_RAW" \
    || echo "Issue importing ${BLOCKCHAIN_RAW}, continuing with monero daemon"

    # These are the entrypoint command and args
    # Add additional args using the CMD field at deploy time
    monerod \
        --non-interactive \
        --p2p-bind-ip 0.0.0.0 \
        --p2p-bind-port $P2P_PORT \
        --rpc-bind-ip 0.0.0.0 \
        --rpc-bind-port $RPC_PORT \
        --confirm-external-bind \
        --data-dir $BLOCKCHAIN_DIRECTORY \
        "$@"
}

main $@
