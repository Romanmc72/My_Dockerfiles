# Raspbian

The Raspbian team has not published a Docker Image to their Docker hub repo in several years. The last known Debian copy is from [stretch / deb 9](https://www.debian.org/releases/stretch/) and now the Debain/Raspbian projects are up to [bullseye / deb 11](https://www.debian.org/releases/bullseye/). This Dockerfile starts with the last published [Raspbian stretch docker image](https://hub.docker.com/r/raspbian/stretch) and upgrades the underlying image to bullseye as a new base image.

## Credit

All credit goes to Mikhail Snetkov <msnetkov@navikey.ru>. I basically ripped [his Dockerfile](https://github.com/navikey/raspbian-bullseye/blob/main/Dockerfile) and added some very minor adjustments