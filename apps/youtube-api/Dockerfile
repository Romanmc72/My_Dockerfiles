FROM python:3.9.7-alpine

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

COPY ./app/main.py /usr/src/app/main.py

RUN adduser --disabled-password appuser appuser && \
    chown -R appuser:appuser /usr/src/app

USER appuser

WORKDIR /usr/src/app

ENV GOOGLE_API_KEY "Set me at runtime"

ENTRYPOINT [ "./main.py" ]

CMD [ "--username", "MrBeast6000" ]
