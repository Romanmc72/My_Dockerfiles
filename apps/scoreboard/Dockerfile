FROM python:3.7.7-alpine
LABEL maintainer "Roman Czerwinski"

COPY ./app/requirements.txt /tmp/requirements.txt 

RUN pip install -r /tmp/requirements.txt

RUN mkdir -p /app/
COPY ./app /app

RUN adduser --disabled-password application_user application_user
USER application_user

WORKDIR /app/

ENV FLASK_APP=/app/scoreboard.py

ENTRYPOINT [ "flask", "run", "--host=0.0.0.0" ]
