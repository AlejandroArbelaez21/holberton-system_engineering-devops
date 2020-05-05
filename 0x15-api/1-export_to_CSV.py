#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID
"""

import csv
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
    name = r.get('name')
    with open('{}.csv'.format(employee_id), 'w', encoding="UTF-8") as file:
        tasks = csv.writer(file, quoting=csv.QUOTE_ALL)
        for task in r_todos:
            tasks.writerow([employee_id, username, task.get('completed'),
                            task.get('title')])
