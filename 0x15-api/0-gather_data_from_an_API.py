#!/usr/bin/python3
"""
using this REST API, for a given employee ID, 
returns information about his/her TODO list progress.
"""

import requests
import sys

API_URL = "https://jsonplaceholder.typicode.com/"

if __name__ == "__main__":
  user = requests.get(API_URL + "users/{}".format(sys.argv[1])).json()
  todos = requests.get(API_URL + "users/{}/todos".format(sys.argv[1])).json()
  completed = [todo for todo in todos if todo["completed"] is True]

  print("Employee {} is done with tasks({}/{}):".format(user.get("name"), len(completed), len(todos)))
  for todo in completed:
    print('\t {}'.format(todo.get('title')))
