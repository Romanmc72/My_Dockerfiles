#!/usr/bin/env python3
"""FastAPI simple app to generate fake data."""
import json
from typing import Optional

from faker import Faker
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
faker = Faker()


class FakeSchematic(BaseModel):
    schematic: Optional[dict] = None


def generate_fake_json(schematic: dict = None):
    """
    Description
    -----------
    Spits out a random json object as a python dict.

    Params
    ------
    :schematic: dict = None
    A dictionary containing the key (returned as is) and the value
    representing the faker data type that you want to get a fake generated
    value for.

    Example input:
    {"my_key": "pyint"}

    Output from example above:
    {"my_key": 8720}

    Default value is:
    {
        "name": "name",
        "residency": "address"
    }

    Return
    ------
    dict
    The dictionary representing the random/fake value you requested.
    """
    if schematic is None or schematic == dict():
        return json.loads(faker.json(num_rows=1))
    else:
        try:
            return json.loads(faker.json(data_columns=schematic, num_rows=1))
        except AttributeError as e:
            return {
                "error": f"Unknown type error",
                "message": repr(e),
                "data": schematic,
            }


@app.get("/")
async def get_data():
    """
    Description
    -----------
    Return fake data to the endpoint.

    Return
    ------
    Default is
    {
        name: faker.name,
        residency: faker.address
    }
    """
    return generate_fake_json()


@app.post("/")
async def custom_fake_data(schematic: FakeSchematic):
    """
    Description
    -----------
    Input a desired fake data format and receive it as json.

    Params
    ------
    :schematic: FakeSchematic
    A dictionary with the following required structure:
    {
        "schematic": {
            "key1": "name",
            "key2": "pyint"
        }
    }

    Return
    ------
    Returns your fake data.

    The above example input will yield:
    {
        "schematic": {
            "key1": "Guy Faker",
            "key2": 1234
        }
    }
    """
    return generate_fake_json(schematic=schematic.schematic)
