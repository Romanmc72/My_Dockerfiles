FROM python:3.8.0-alpine
# For this to run, you will need to override some env variables and do a volume mount to the flask application.
# volumes:
#     - /location/on/disk/where/flask_app:/usr/src/app
# And this program does expect your application to be called `flask_app.py`

# In order to use postgres, you need the psycopg2 from pip,
# but in order to install that you need all of this junk
RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev

# Nobody likes you when you run under root
RUN adduser --disabled-password flask_user flask_user 
USER flask_user

# Set the working directory
WORKDIR /usr/src/app

# All the libraries for flask to run
COPY requirements.txt /tmp/requirements.txt
RUN pip install --user --upgrade pip && \
    pip install --user -r /tmp/requirements.txt

# Nobody wants to see your .pyc files
ENV PYTHONDONTWRITEBYTECODE 1

# Unbuffer the stdout and stderr streams
ENV PYTHONUNBUFFERED 1

# This is required for the pip installed requirements to find
# the `flask` executable when the entrypoint is run
ENV PATH=/home/flask_user/.local/bin:$PATH

# Required for flask to run
ENV FLASK_APP=/usr/src/app/flask_app.py

# Override these otherwise it will not work
ENV DATABASE_URI "postgresql+psycopg2://username:password@server_name:port/db"
ENV MAIL_SERVER mail.server.name
ENV MAIL_PORT 123
ENV MAIL_USE_TLS 1
ENV MAIL_USERNAME username
ENV MAIL_PASSWORD password

COPY wait_for_postgres.py /home/flask_user/wait_for_postgres.py
COPY entrypoint.sh /home/flask_user/entrypoint.sh

ENTRYPOINT [ "/home/flask_user/entrypoint.sh" ]
