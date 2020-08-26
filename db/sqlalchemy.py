#!/usr/bin/env python3
"""
This will create a connection to the
postgres database on localhost and
create a table called students
"""
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer

db_string = "postgres://flask:not_the_password@localhost:5432/flask_db"
db = create_engine(db_string)
meta_data = MetaData()
students = Table(
    'students',
    meta_data,
    Column('id', Integer, primary_key = True),
    Column('firstname', String),
    Column('lastname', String),
    schema='flask_app'
)
meta_data.create_all(db)
