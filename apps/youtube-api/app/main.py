#!/usr/bin/env python3
"""
Description
-----------
Fetches the Youtube subscriber count for a particular youtube channel.

To find someones username or id, simply visit their channel on YouTube and in
the URL you will either see something like this:

https://www.youtube.com/c/MrBeast6000
                          ^^^^^^^^^^^
                          | This is  |
                          | the      |
                          | username |
                          +----------+

OR something like this:

https://www.youtube.com/channel/UCY1kMZp36IQSyNx_9h4mpCg
                                ^^^^^^^^^^^^^^^^^^^^^^^^
                                | This is the id.      |
                                +----------------------+
"""
import os

import googleapiclient.discovery

API_KEY = os.getenv("GOOGLE_API_KEY", "Set me in the Environment!")


def get_title_and_subscriber_count(
    username: str = None, id: str = None, api_key: str = API_KEY
) -> None:
    """
    Description
    -----------
    Gets the channel title and subscriber count for a youtube channel based on
    the channel username or the channel ID.

    Params
    ------
    :username: str = None
    The username of the channel if one exists.

    :id: str = None
    The id of the channel.

    If both arguments are supplied, the username will be used and the id will
    be ignored.

    Return
    ------
    tuple
    (title: str, subscriber_count: int)
    """
    api_service_name = "youtube"
    api_version = "v3"
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=api_key
    )

    args = {"part": "brandingSettings,statistics"}

    if username:
        args["forUsername"] = username
    elif id:
        args["id"] = id
    else:
        raise TypeError("Missing one of two positional arguments, username OR id.")

    response = call_api_client(client=youtube, args=args)
    title = response["items"][0]["brandingSettings"]["channel"]["title"]
    subscriber_count = int(response["items"][0]["statistics"]["subscriberCount"])
    return title, subscriber_count


def call_api_client(client=None, args: dict = None) -> dict:
    """
    Description
    -----------
    Given the client, call the api to get the channel details.

    Params
    ------
    :client: dicovery.build object = None
    Should be the instantiated and authenticated client.

    :args: dict = None
    The arguments that will be passed to the API.

    Return
    ------
    dict
    The response dict.
    """
    request = client.channels().list(**args)
    response = request.execute()
    return response


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "--username",
        type=str,
        help="The username for the youtube channel to fetch subscriber count from. E.g. 'MrBeast6000' for Mr Beast",
    )
    group.add_argument(
        "--id",
        type=str,
        help="The id for the youtube channel to fetch subscriber count from. E.g. 'UCY1kMZp36IQSyNx_9h4mpCg' for Mark Rober.",
    )
    args = parser.parse_args()
    title, subscriber_count = get_title_and_subscriber_count(
        username=args.username, id=args.id
    )
    print(f"{title} currently has {subscriber_count:,} subscribers.")
