#!/usr/bin/python3
"""export data in the CSV format."""

import csv
import requests
import sys

API_URL = "https://jsonplaceholder.typicode.com/"

if __name__ == "__main__":
    user = requests.get(API_URL + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(API_URL + "users/{}/todos".format(sys.argv[1])).json()

    with open("{}.csv".format(user.get("id")), "w", newline="") as file:
        author = csv.writer(file, quoting=csv.QUOTE_ALL)
        [author.writerow([sys.argv[1], user.get("username"), todo.get(
            "completed"), todo.get("title")]) for todo in todos]
