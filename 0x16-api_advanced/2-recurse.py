#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    queries the Reddit API and returns a list containing the titles of all hot articles for a given subreddit. If no results are found for the given subreddit, the function should return None.

    Hint: The Reddit API uses pagination for separating pages of responses.

    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): A list used to accumulate the titles of hot articles.
        after (str): A string token indicating the start of the next page of results.

    Returns:
        list: A list of title strings for hot articles in the specified subreddit,
        or None if the subreddit is invalid or no results are found.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "0x16-api_advanced_project_v1"}
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
