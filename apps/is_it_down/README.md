# IS IT DOWN

Well, is it?!?

I made this image to run on my local home cluster to ping my garage door opener and see how frequently it is actually unreachable in my home network. Essentially it will do one ping, log the result to postgres, sleep for 5 minutes then repeat forever. After a little while I plan to take a look at the results of this chart over time to see if there are any trends I can decipher or if it is just really inconsistently available.

I replaced my router [with this one](https://www.amazon.com/MOTOROLA-MG7700-AC1900-Gigabit-Maximum/dp/B07BRZ2KW5/ref=sr_1_3?keywords=MOTOROLA+WiFi+Router&qid=1637331990&qsid=142-3922032-2306304&sr=8-3&sres=B07BRZ2KW5%2CB08DL4QB25%2CB07CDQNHRX%2CB01JGT2JI6%2CB09GWFYTCY%2CB08XLBH2M9%2CB08B73VDZL%2CB088KW4FN3%2CB088KVGSTC%2CB07JN8B3GZ%2CB09HZ7KLZX%2CB077NNGNJM%2CB0723599RQ%2CB01A1E6BA2%2CB09HL4RLRV%2CB079JD7F7G&srpt=NETWORKING_ROUTER) to avoid paying the rental fees to the cable company. The cable company's router used to reach my garage just fine however this new one seems to be a little less capable. If it cannot get the job done I will need to get a new one.

## Running this

I will be publishing this image to dockerhub, so feel free to download it from there or build it here yourself. To run it you will need to set a few env vars.

```bash
docker run \
    --rm \
    -e SLEEP_INTERVAL="<YOUR-SLEEP_INTERVAL>" \        # default: 300 seconds between pings, INT
    -e IP_TO_PING="<YOUR-IP_TO_PING>" \                # default: "0.0.0.0", STR
    -e POSTGRES_HOST="<YOUR-POSTGRES_HOST>" \          # default: "localhost", STR
    -e POSTGRES_PORT="<YOUR-POSTGRES_PORT>" \          # default: "5432", INT
    -e POSTGRES_USERNAME="<YOUR-POSTGRES_USERNAME>" \  # default: "flask", STR
    -e POSTGRES_PASSWORD="<YOUR-POSTGRES_PASSWORD>" \  # default: "not_the_password", STR
    -e POSTGRES_DBNAME="<YOUR-POSTGRES_DBNAME>" \      # default: "dev", STR
    -e POSTGRES_SCHEMA="<YOUR-POSTGRES_SCHEMA>" \      # default: "public", STR
    -e POSTGRES_TABLE="<YOUR-POSTGRES_TABLE>" \        # default: "is_it_down", STR
    -e ITERATIONS_TO_RUN="<YOUR-ITERATIONS_TO_RUN>" \  # default: -1 (how many times to ping before exiting, value <= 0 means run forever), INT
    romanmc72/is_it_down:latest
```

The postgres table you are writing to should have the following schema:

```SQL
CREATE TABLE IF NOT EXISTS public.is_it_down (
  id SERIAL PRIMARY KEY,
  ping_timestamp NUMERIC(17, 6) NOT NULL,
  host_was_reachable BOOLEAN NOT NULL,
  hostname VARCHAR(256) NOT NULL
);
```
