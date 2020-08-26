#!/usr/bin/env python3
"""
PostgreSQL must be ready to receive connections before flask can start issuing commands to it.
This application loops until that is tha case then exits.
"""
import os
import time

from sqlalchemy import exc
from sqlalchemy import create_engine


NGN = os.getenv('DATABASE_URI', 'postgresql+psycopg2://flask:not_the_password@webserver_db_1:5432/flask_db')

while 1:
    try:
        e = create_engine(NGN)
        e.execute('select 1')
    except exc.OperationalError:
        print('Waiting for database...')
        time.sleep(1)
    else:
        break

print('Connected!')
