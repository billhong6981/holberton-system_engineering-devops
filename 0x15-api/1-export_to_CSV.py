#!/usr/bin/python3
"""a module that request data and save in csv format"""
import csv
import json
import requests
from sys import argv


if __name__ == "__main__":
    if argv[1] is None or type(int(argv[1])) is not int:
        exit()
    filename = argv[1] + ".csv"
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
    EMPLOYEE_NAME = user.get("username", None)

    with open(filename, "w") as f:
        csv_fields = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                      "TASK_TITLE"]
        writer = csv.DictWriter(f, fieldnames=csv_fields)
        writer.writeheader()
        for thing in things:
            row_dict = {}
            if thing.get("userId", None) == int(argv[1]):
                row_dict["USER_ID"] = thing.get("userId", None)
                row_dict["USERNAME"] = EMPLOYEE_NAME
                row_dict["TASK_COMPLETED_STATUS"] = thing.get("completed")
                row_dict["TASK_TITLE"] = thing.get("title", None)
                json.dumps(row_dict)
                writer.writerow(row_dict)
