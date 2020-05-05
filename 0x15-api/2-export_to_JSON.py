#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID
"""

import json
import requests
from sys import argv

""" This prevent that my code not be executed when imported """
if __name__ == "__main__":
    """The funtion"""
    employee_id = argv[1]
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(
        employee_id)).json()
    username = r.get('username')
    r_todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
         employee_id)).json()
    my_list = []
    my_dict = {employee_id: my_list}
    for items in r_todos:
        other_dict = {}
        other_dict["task"] = items.get("title")
        other_dict["completed"] = items.get("completed")
        other_dict["username"] = username
        my_list.append(other_dict)
    with open("{}.json".format(employee_id), 'w', encoding="utf-8") as file:
        file.write(json.dumps(my_dict))
    