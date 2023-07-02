# Ripped this off of
# https://github.com/navikey/raspbian-bullseye/blob/main/Dockerfile
# Starting with raspbian stretch, the last maintained/pushed Docker image form
# ~4 years ago as of writing this
FROM raspbian/stretch:latest AS raspbian-stretch-upgrade

ENV DEBIAN_FRONTEND noninteractive

RUN true \
	# Stops the background services from starting and restarting during the
    # install/upgrade process
    # https://jpetazzo.github.io/2013/10/06/policy-rc-d-do-not-start-services-automatically/
	&& echo -e '#!/bin/sh\nexit 101' > /usr/sbin/policy-rc.d \
	&& chmod +x /usr/sbin/policy-rc.d \
	&& apt-get update \
	&& apt-get upgrade -y \
	&& apt-get full-upgrade -y \
	&& apt-get autoremove --purge -y \
	&& apt-get clean -y \
	# Switch to Bullseye repository.
	&& sed -i 's/stretch/bullseye/g' /etc/apt/sources.list \
	&& apt-get update \
	&& apt-get upgrade -y \
	&& apt-get full-upgrade -y \
	&& apt-get autoremove --purge -y \
	&& apt-get clean -y \
	# Remove files outside base image.
	&& rm -rf /var/lib/apt/lists/* \
	&& rm -f /usr/sbin/policy-rc.d

# Restart from scratch
FROM scratch

LABEL maintainer="Roman Czerwinski<romanmc72@gmail.com>"

# Take the entire image contents from the first step of the build and copy
# over to the scratch image
COPY --from=raspbian-stretch-upgrade / /

# Add the pi user and its home directory
RUN mkdir /home/pi \
    && groupadd pi \
    && useradd pi \
        --gid pi \
        --base-dir /home/pi \
        --password password \
        --shell /bin/bash \
    && chown pi:pi /home/pi
