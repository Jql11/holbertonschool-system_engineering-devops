#!/usr/bin/python3
"""
export to csv
"""
import requests as req
import sys
import csv

if __name__ == "__main__":
    USER_ID = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    response = req.get(url + 'users/{}'.format(USER_ID))
    todo = req.get(url + 'todos?userId={}'.format(USER_ID))
    USERNAME = response.json().get('username')

    f = open('{}.csv'.format(USER_ID), 'w')
    writer = csv.writer(f)
    for task in todo.json():
        TASK_COMPLETED_STATUS = task.get('completed')
        TASK_TITLE = task.get('title')
        writer.writerow([USER_ID, USERNAME, TASK_COMPLETED_STATUS, TASK_TITLE])
    f.close()
