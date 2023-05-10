#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the first 10 hot posts.
"""

import requests


def top_ten(subreddit):
    """
    queries the Reddit API and prints the titles of the first 10 hot posts listed for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "0x16-api_advanced_project_v1"}
    params = {'limit': 10}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts[:10]:
            print(post["data"]["title"])
    else:
        print(None)
