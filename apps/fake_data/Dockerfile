FROM python:3.9.7

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY app /usr/src/app

WORKDIR /usr/src/app

RUN useradd fastapi && chown -R fastapi:fastapi /usr/src/app
USER fastapi

# This assumes that your python file is called `main.py`
# and the FastAPI app therin is called `app`
ENTRYPOINT [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]
