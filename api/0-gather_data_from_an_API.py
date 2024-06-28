#!/usr/bin/python3
"""
Uses https://jsonplaceholder.typicode.com along with an employee ID to
return information about the employee's todo list progress.
"""

import requests
from sys import argv

if __name__ == '__main__':
    user_id = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(user_id)).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)).json()
    
    completed_tasks = [task.get('title') for task in todos if task.get('completed') is True]
    
    print("Employee {} is done with tasks({}/{}):".format(user.get('name'), len(completed_tasks), len(todos)))
    for task in completed_tasks:
        print("\t {}".format(task))
