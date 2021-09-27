# Fake Data

This is a Python API that exists to generate fake data. It runs FastAPI and uvicorn.

## Running The Container

you can run it locally with docker like so:

```bash
docker run --rm -d -p 8000:8000 romanmc72/fake-data-api:0.0.1
```

You issue a `GET` to get the following schema:

```JSON
{
    "name": "name",
    "residency": "address"
}
```

or if you issue a `POST` request you can pass in a different schema and receive the fake data for that schema. Example:

```JSON
{
    "schematic": {
        "name": "name",
        "poops_this_year": "pyint"
    }
}
```

This will return something like:

```JSON
{
    "name": "Guy Faker",
    "poops_this_year": 6092
}
```

## Other options

This can also be run in the cloud in any container runtime that you like. If you want to change the port assignments (instead of `8000`), you can rewrite the `entrypoint` argument to change the `--port` argument. As it stands it is running like so:

```Dockerfile
# This assumes that your python file is called `main.py`
# and the FastAPI app therin is called `app`
ENTRYPOINT [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]
```
