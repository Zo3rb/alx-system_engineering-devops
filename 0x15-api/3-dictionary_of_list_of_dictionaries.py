#!/usr/bin/python3
"""export data in the JSON format."""

import json
import requests

API_URL = "https://jsonplaceholder.typicode.com/"

if __name__ == "__main__":
    users = requests.get(API_URL + "users").json()

    with open("todo_all_employees.json", "w") as file:
        json.dump({
            user['id']: [{"username": user['username'], "task": res['title'], "completed": res['completed']} for res in requests.get(API_URL + "users/{}/todos".format(user['id'])).json()] for user in users}, file)
