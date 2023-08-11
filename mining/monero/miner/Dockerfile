FROM alpine:3.18.2

LABEL maintainer="RomanMC72 (Roman Czerwinski)"

# Build the mining software from source, copied from here
# https://xmrig.com/docs/miner/build/alpine
# Requirements:
RUN apk update \
    && apk add \
    cmake \
    g++ \
    gcc \
    git \
    hwloc-dev \
    libstdc++ \
    libuv-dev \
    make \
    openssl-dev \
    wget

# Acutally building the program from source:
RUN git clone https://github.com/xmrig/xmrig \
    && mkdir xmrig/build && cd xmrig/build \
    && cmake .. \
    && make -j$(nproc) \
    && cp ./xmrig /usr/bin/xmrig \
    && echo vm.nr_hugepages=1280 >> /etc/sysctl.conf

# Do not run the container as root!
RUN addgroup miner-mike \
    && adduser miner-mike -D -G miner-mike

USER miner-mike
WORKDIR /home/miner-mike

# Using a config file instead of command line arguments is the preferred way
# to manage the miner and its settings with the greatest amount of control.
# The config is in this build directory and the specs can be found here:
# https://xmrig.com/docs/miner/config
# Also there is a setup wizard you can use
COPY ./config.json /home/miner-mike/config.json

ENTRYPOINT [ "xmrig" ]
CMD [ "--config", "./config.json" ]
