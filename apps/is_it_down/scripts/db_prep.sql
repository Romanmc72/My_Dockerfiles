/*
 * These were the ad hoc SQL commands required to run for the default env vars
 * to work on my default postgres testing setup.
 */
CREATE DATABASE dev;

USE dev;

CREATE TABLE IF NOT EXISTS public.is_it_down (
  id SERIAL PRIMARY KEY,
  ping_timestamp NUMERIC(17, 6) NOT NULL,
  host_was_reachable BOOLEAN NOT NULL,
  hostname VARCHAR(256) NOT NULL
);
