FROM python:3.7.7-alpine
LABEL maintainer "Roman Czerwinski"

COPY ./app/requirements.txt /tmp/requirements.txt 

RUN pip install -r /tmp/requirements.txt && pip install gunicorn==20.0.4

RUN mkdir -p /app/
COPY ./app /app
COPY ./logging.ini /app/logging.ini

RUN adduser --disabled-password application_user application_user
USER application_user

WORKDIR /app/

ENV FLASK_APP=/app/scoreboard.py

# Added a logging config to get flask logs to stdout in the container.
ENTRYPOINT [ "gunicorn", "--workers=2", "--bind=0.0.0.0:5000", "--access-logfile=-", "--log-config=logging.ini", "scoreboard:app" ]
