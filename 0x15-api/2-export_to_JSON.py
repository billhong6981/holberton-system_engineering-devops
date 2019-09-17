#!/usr/bin/python3
"""a module that request data and save in json format"""
import requests
from sys import argv
import csv
import json


if __name__ == "__main__":
    if argv[1] is None:
        exit()
    filename = argv[1] + ".json"
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
    EMPLOYEE_NAME = user.get("name")
    row = {}
    with open(filename, "w") as f:
        json_list = []
        for thing in things:
            row_dict = {}
            if thing["userId"] == int(argv[1]):
                row_dict["task"] = thing["title"]
                row_dict["completed"] = thing["completed"]
                row_dict["username"] = user["username"]
                json_list.append(row_dict)
        row[str(argv[1])] = json_list
        json.dumps(row)
        f.write(str(row))
