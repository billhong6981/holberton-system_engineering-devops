#!/usr/bin/python3
"""a module that request data and save in csv format"""
import requests
from sys import argv
import csv
import json


if __name__ == "__main__":
    if argv[1] is None:
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
    EMPLOYEE_NAME = user.get("username")

    with open(filename, "w") as f:
        csv_fields = ["USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"]
        writer = csv.DictWriter(f, fieldnames=csv_fields)
        writer.writeheader()
        for thing in things:
            row_dict = {}
            if thing["userId"] == int(argv[1]):
                row_dict["USER_ID"] = thing["userId"]
                row_dict["USERNAME"] = EMPLOYEE_NAME
                row_dict["TASK_COMPLETED_STATUS"] = thing["completed"]
                row_dict["TASK_TITLE"] = thing["title"]
                writer.writerow(row_dict)
