#!/usr/bin/python3
"""
using this REST API
must use urllib or requests module
"""
import requests as req
import sys

if __name__ == "__main__":
    employee_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    response = req.get(url + 'users/{}'.format(employee_id))
    todo = req.get(url + 'todos?userId={}'.format(employee_id))
    total_task = 0
    completed_task = 0
    TASK_TITLE = []
    for task in todo.json():
        total_task += 1
        if (task.get('completed') is True):
            completed_task += 1
            TASK_TITLE.append(task.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(
        response.json().get('name'), completed_task, total_task))
    for item in TASK_TITLE:
        print("\t{}".format(item))
