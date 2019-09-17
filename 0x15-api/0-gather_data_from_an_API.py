#!/usr/bin/python3
"""a module that request data via REST API service"""
import requests
from sys import argv


if __name__ == "__main__":
    if argv[1] is None or type(int(argv[1])) is not int:
        exit()
    url = "https://jsonplaceholder.typicode.com"
    try:
        res_user = requests.get(url + "/users/" + argv[1])
        user = res_user.json()
    except:
        exit()
    try:
        res_todo = requests.get(url + "/todos")
        things = res_todo.json()
    except:
        exit()
    EMPLOYEE_NAME = user.get("name", None)
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []

    for thing in things:
        if thing.get("userId", None) == int(argv[1]):
            TOTAL_NUMBER_OF_TASKS += 1
            if thing.get("completed", None) is True:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(thing.get("title", None))
    print("Employee {} is done with tasks({}/{}):"
          .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for task in TASK_TITLE:
        print("\t{}".format(task))
