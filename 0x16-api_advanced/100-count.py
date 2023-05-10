#!/usr/bin/python3
"""
This module defines a recursive function `count_words` that queries the Reddit API,
parses the title of all hot articles, and prints a sorted count of given keywords.
"""

import requests

def count_words(subreddit, word_list, after=None, word_dict={}):
    """
    Recursively retrieves all hot articles for the given subreddit, parses their titles,
    and counts the occurrences of each keyword in the titles. Prints a sorted count of
    each keyword to standard output.

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): A list of lowercase strings representing the keywords to count.
        after (str): A string token indicating the start of the next page of results.
        word_dict (dict): A dictionary used to accumulate the counts of each keyword.

    Returns:
        None
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "MyBot/0.0.1"}
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            title_words = post["data"]["title"].lower().split()
            for word in word_list:
                if word in title_words and len(word) > 2:
                    if word not in word_dict:
                        word_dict[word] = 1
                    else:
                        word_dict[word] += 1
        if data["data"]["after"] is not None:
            return count_words(subreddit, word_list, data["data"]["after"], word_dict)
        else:
            sorted_words = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_words:
                print(f"{word}: {count}")
    else:
        print(None)

