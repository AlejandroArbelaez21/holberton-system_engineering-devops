#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID
"""


import requests
from sys import argv

""" This prevent that my code not be executed when imported """
if __name__ == "__main__":
    """The funtion"""
    employee_id = argv[1]
    r = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(
        employee_id)).json()
    r_todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
         employee_id)).json()
    name = r.get('name')
    titles = []
    titles_com = []
    n = 0
    for task in r_todos:
        titles.append(task.get('title'))
        if task['completed'] is True:
            n += 1
            titles_com.append(task.get('title'))
    print("Employee {} is done with tasks({}/{})".format(name, n, len(titles)))
    for title in titles_com:
        print("\t {}".format(title))
