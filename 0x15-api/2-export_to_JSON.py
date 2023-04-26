#!/usr/bin/python3
"""export data in the JSON format."""

import json
import requests
import sys

API_URL = "https://jsonplaceholder.typicode.com/"

if __name__ == "__main__":
    user = requests.get(API_URL + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(API_URL + "users/{}/todos".format(sys.argv[1])).json()

    with open("{}.json".format(user.get("id")), "w") as file:
        json.dump({sys.argv[1]: [{"task": todo.get("title"), "completed": todo.get("completed"), "username": user.get("username")} for todo in todos]}, file)

