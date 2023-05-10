#!/usr/bin/python3
"""
This module defines a recursive function `recurse` that queries the Reddit API
and returns a list containing the titles of all hot articles for a given subreddit.
"""

import requests

def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively retrieves all hot articles for the given subreddit and returns
    them as a list of title strings.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): A list used to accumulate the titles of hot articles.
        after (str): A string token indicating the start of the next page of results.

    Returns:
        list: A list of title strings for hot articles in the specified subreddit,
        or None if the subreddit is invalid or no results are found.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyBot/0.0.1"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            hot_list.append(post["data"]["title"])
        if data["data"]["after"] is not None:
            return recurse(subreddit, hot_list, data["data"]["after"])
        else:
            return hot_list
    else:
        return None

