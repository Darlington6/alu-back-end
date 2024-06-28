#!/usr/bin/python3
"""
Uses https://jsonplaceholder.typicode.com along with an employee ID to
return information about the employee's todo list progress.
"""

import requests
from sys import argv

if __name__ == '__main__':
    if len(argv) < 2:
        print("Usage: ./script.py <employee_id>")
        exit(1)

    user_id = argv[1]
    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

    user = requests.get(user_url, verify=False).json()
    todos = requests.get(todo_url, verify=False).json()

    completed_tasks = [task['title'] for task in todos if task.get('completed')]

    employee_name = user.get('name')
    total_tasks = len(todos)
    completed_count = len(completed_tasks)

    print(f"Employee {employee_name} is done with tasks({completed_count}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t {task}")
