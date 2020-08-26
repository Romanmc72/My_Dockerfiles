FROM postgres:12.0-alpine
ENV POSTGRES_DB flask_db
COPY postgres_schema.sql /docker-entrypoint-initdb.d/
