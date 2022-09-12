#!/usr/bin/python3
"""
export data in the JSON format
"""
import json
import requests as req

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    response = req.get(url + 'users')

    users = {}
    for user in response.json():
        user_id = user.get('id')
        USERNAME = user.get('username')
        todo = req.get(url + 'todos?userId={}'.format(user_id))
        tasks = []
        for task in todo.json():
            dictionary = {}
            TASK_COMPLETED_STATUS = task.get('completed')
            TASK_TITLE = task.get('title')
            dictionary["username"] = USERNAME
            dictionary["task"] = TASK_TITLE
            dictionary["completed"] = TASK_COMPLETED_STATUS
            tasks.append(dictionary)
        users[user_id] = tasks

    with open("todo_all_employees.json", "w") as outfile:
        json.dump(users, outfile)
