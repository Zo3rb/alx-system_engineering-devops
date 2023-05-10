#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subscribers
    If an invalid subreddit is given, the function returns 0.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers for the given subreddit, or 0 if the
        subreddit is invalid.
    """
    url = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "0x16-api_advanced_project_v1"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]
    else:
        return 0
