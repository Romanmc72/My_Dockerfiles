#!/usr/bin/env python3
"""Runs the statistics query to see where the experiment is currently at"""
import os
import json

import psycopg2


def print_analysis():
    """Simply runs the analysis query and prints the results"""
    connection = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "0.0.0.0"),
        port=int(os.getenv("POSTGRES_PORT", 5432)),
        user=os.getenv("POSTGRES_USER", "flask"),
        password=os.getenv("POSTGRES_PASSWORD", "not_the_password"),
        dbname=os.getenv("POSTGRES_DBNAME", "dev"),
    )

    with open("./analysis.sql", "r") as sql_file:
        sql = sql_file.read()
    try:
        with connection:
            with connection.cursor() as cursor:
                cursor.execute(sql)
                rows = cursor.fetchall()
                column_names = [column[0] for column in cursor.description]
    finally:
        connection.close()
    jsonified_data = [dict(zip(column_names, row)) for row in rows]
    print(json.dumps(jsonified_data, indent=4, default=str))


if __name__ == "__main__":
    print_analysis()
