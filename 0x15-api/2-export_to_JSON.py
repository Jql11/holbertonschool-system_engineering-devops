#!/usr/bin/python3
"""
export to csv
"""
import csv
import json
import requests as req
import sys

if __name__ == "__main__":
    USER_ID = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    response = req.get(url + 'users/{}'.format(USER_ID))
    todo = req.get(url + 'todos?userId={}'.format(USER_ID))
    USERNAME = response.json().get('username')

    with open("{}.json".format(USER_ID), "w") as outfile:
        tasks = []
        for task in todo.json():
            dictionary = {}
            TASK_COMPLETED_STATUS = task.get('completed')
            TASK_TITLE = task.get('title')
            dictionary["task"] = TASK_TITLE
            dictionary["completed"] = TASK_COMPLETED_STATUS
            dictionary["username"] = USERNAME
            tasks.append(dictionary)
        output = {
                "{}".format(USER_ID): tasks
        }
        json.dump(output, outfile)
