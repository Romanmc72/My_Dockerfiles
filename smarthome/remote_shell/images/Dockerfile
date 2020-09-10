FROM python:3.8-alpine

RUN apk update && \
    apk add \
        --no-cache \
        --virtual \
        .pynacl_deps \
        build-base \
        python3-dev \
        libffi-dev \
        openssl-dev \
        py3-paramiko

COPY ./requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

COPY ./app.py /usr/src/app.py 

ENV USERNAME="not_the_user"
ENV HOSTNAME="0.0.0.0"
ENV PASSWORD="not_the_password"

ENTRYPOINT ["python", "/usr/src/app.py"]
