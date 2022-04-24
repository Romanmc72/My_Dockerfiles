FROM python:3.9.9

RUN apt-get update && \
    apt-get install inetutils-ping

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

RUN groupadd ping_worker && \
    useradd -g ping_worker ping_worker

USER ping_worker

WORKDIR /usr/src

COPY ./app/main.py /usr/src/main.py

ENTRYPOINT [ "./main.py" ]
