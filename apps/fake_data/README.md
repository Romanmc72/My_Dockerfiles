# Fake Data

This is a Python API that exists to generate fake data. It runs FastAPI and uvicorn locally or in an environment like k8s/docker. There is an image here as well built for use on AWS lambda specifically.

Images are published to the following repositories:

```
# Docker
romanmc72/fake-data-api:#.#.#

# AWS - lambda specifically
005071865344.dkr.ecr.us-east-1.amazonaws.com/r0m4n.com/fake-data-api:#.#.#
```

## Running The Container Locally

you can run it locally with docker like so:

```bash
# Specify which tag you wish to run
./up.sh "#.#.#"
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

## Running The Container On AWS Lambda

I have a separate repository devoted to standing up the Lambda function and AWS API Gateway using Hashicorp's [Terraform](https://www.terraform.io/) tool. That repositry and associated code live [here](https://github.com/Romanmc72/terraform-setup/tree/main/lambda). See that readme for how to use it.

## Other options

This can also be run in the cloud in any container runtime that you like. If you want to change the port assignments (instead of `8000`), you can rewrite the `entrypoint` argument to change the `--port` argument. As it stands it is running like so:

```Dockerfile
# This assumes that your python file is called `main.py`
# and the FastAPI app therin is called `app`
ENTRYPOINT [ "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000" ]
```
