#!/usr/bin/env python3
"""
Description
-----------
This program pings an IP or hostname provided to see if it is up, then log the
results to postgres and waits for the next run.
"""
import logging
import os
import subprocess
import sys
import textwrap
from datetime import datetime
from time import sleep

import psycopg2
from psycopg2 import OperationalError, connect

log_format = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
stdout_log_stream = logging.StreamHandler(sys.stdout)
stdout_log_stream.setFormatter(log_format)
logger = logging.Logger(name="is_it_down", level=logging.INFO)
logger.addHandler(stdout_log_stream)

# You should set these variables in the environment to run this
SLEEP_INTERVAL = int(os.getenv("SLEEP_INTERVAL", 300))
IP_TO_PING = os.getenv("IP_TO_PING", "0.0.0.0")
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "localhost")
POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", "5432"))
POSTGRES_USERNAME = os.getenv("POSTGRES_USERNAME", "flask")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD", "not_the_password")
POSTGRES_DBNAME = os.getenv("POSTGRES_DBNAME", "dev")
POSTGRES_SCHEMA = os.getenv("POSTGRES_SCHEMA", "public")
POSTGRES_TABLE = os.getenv("POSTGRES_TABLE", "is_it_down")

# Only set this if you want it to exit after a certain number of iterations
ITERATIONS_TO_RUN = int(os.getenv("ITERATIONS_TO_RUN", -1))


def execute(
    interval: int = SLEEP_INTERVAL, iterations: int = ITERATIONS_TO_RUN
) -> None:
    """The main program to be executed at runtime."""
    wait_for_postgres_to_be_available()
    ensure_table_exists()
    counter = 0
    while True:
        ping_response = ping_the_ip()
        submit_response_to_postgres(ping_response)
        if iterations > 0:
            counter += 1
            if counter > iterations:
                break
        logger.info(f"Successfully ping'd {IP_TO_PING}. Sleeping for {interval}...")
        sleep(interval)


def wait_for_postgres_to_be_available(
    timeout: int = 300, sleep_seconds: int = 5
) -> None:
    """
    Description
    -----------
    Because certain containers may start before others, this will allow
    `is_it_down` to wait for the db to be up before failing. It will timeout
    at 5 minutes by default.

    Params
    ------
    :timeout: int = 300
    How many seconds to wait before throwing up your hands and quitting.

    :sleep_seconds: int = 5
    The period of time to wait before trying again. Measured in seconds.

    Return
    ------
    None
    """
    timer = 0
    connected = False
    while not connected:
        try:
            execute_sql("SELECT 1")
            connected = True
        except OperationalError as e:
            logger.warning(f"Postgres not reachable: {repr(e)}")
            logger.warning("Waiting a little bit then trying again...")
            sleep(sleep_seconds)
            timer += sleep_seconds
            if timer >= timeout:
                logger.error(
                    f"Database unreachable after `{timer}` seconds of timeout set at `{timeout}` seconds."
                )
                raise e
    logger.info("Connected!")


def ensure_table_exists():
    """Before you start writing to a database, the table should probably be there."""
    execute_sql(
        textwrap.dedent(
            f"""\
            CREATE TABLE IF NOT EXISTS "{POSTGRES_SCHEMA}"."{POSTGRES_TABLE}" (
                id                 SERIAL PRIMARY KEY,
                ping_timestamp     NUMERIC(17, 6) NOT NULL,
                host_was_reachable BOOLEAN NOT NULL,
                hostname           VARCHAR(256) NOT NULL
            );"""
        )
    )


def get_postgres_connection():
    """DRY connect to postgres method."""
    logger.info("Connecting to DB...")
    return psycopg2.connect(
        host=POSTGRES_HOST,
        port=POSTGRES_PORT,
        user=POSTGRES_USERNAME,
        password=POSTGRES_PASSWORD,
        dbname=POSTGRES_DBNAME,
    )


def execute_sql(sql: str, params: tuple = None) -> None:
    """
    Description
    -----------
    Wrapper for connecting, opening cursor, executing, committing, and
    closing the connection.

    Params
    ------
    :sql: str
    The string representing the SQL command you wish to run.

    :params: tuple
    A tuple of any parameters for the SQL.

    Return
    ------
    None
    """
    connection = get_postgres_connection()
    try:
        with connection:
            with connection.cursor() as cursor:
                logger.info(f"Running SQL: ```{sql}``` with params: ```{params}```...")
                cursor.execute(sql, params)
                logger.info("Committing transaction...")
                connection.commit()
                logger.info("Committed transaction.")
    finally:
        logger.info("Closing DB connection...")
        connection.close()
        logger.info("Closed DB connection.")


def ping_the_ip(ip: str = IP_TO_PING) -> bool:
    """Pings an IP and either exits successfully or unsuccessfully"""
    cmd = ["/bin/ping", "-c", "1", ip]
    logger.info(f"Pinging {ip}...")
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    logger.info(f"Logging responses {ip}...")
    logger.info(stdout.decode())
    if stderr:
        logger.error(stderr.decode())
    is_it_running = process.returncode == 0
    logger.info(f"Is {ip} running? : {is_it_running}")
    return is_it_running


def submit_response_to_postgres(ping_response: bool, ip: str = IP_TO_PING) -> None:
    """
    Connects to Postgres and writes whether the response was successful or
    unsuccessful along with the timestamp and the ip/hostname.
    """
    current_time = datetime.utcnow().timestamp()
    sql = textwrap.dedent(
        f"""\
        INSERT INTO
            {POSTGRES_SCHEMA}.{POSTGRES_TABLE} (ping_timestamp, host_was_reachable, hostname)
        VALUES
            (%s, %s, %s)
        ;"""
    )
    params = (current_time, ping_response, ip)
    execute_sql(sql, params)


if __name__ == "__main__":
    logger.info("Beginning execution...")
    execute()
    logger.info("Finished executing.")
