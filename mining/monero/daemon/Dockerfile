FROM alpine:3.18.2

LABEL maintainer="RomanMC72 (Roman Czerwinski)"

# Although not the officially supported source, it does all the same things
# and installs significantly faster than building from source
RUN apk update && apk add monero

# Never run your container as the root user!
RUN addgroup monerod && adduser monerod -D -G monerod

# These are the standard ports, but can be overridden using env vars
# See these standard ports and other defaults by running `monerod --help`
ENV P2P_PORT=18080
ENV RPC_PORT=18081
ENV BLOCKCHAIN_DIRECTORY="/home/monerod"
ENV BLOCKCHAIN_RAW=$BLOCKCHAIN_DIRECTORY/blockchain.raw

# Ideally this is mounted at runtime to some durable storage so that the
# blockchain does not need to be fully redownloaded on restarts
VOLUME [ "/home/monerod" ]
COPY ./entrypoint.sh /opt/entrypoint.sh
RUN chown monerod:monerod /opt/entrypoint.sh

USER monerod
WORKDIR /home/monerod

# CMD args for the monerod program can be passed to this script
ENTRYPOINT exec sh /opt/entrypoint.sh
