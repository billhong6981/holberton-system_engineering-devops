#!/usr/bin/python3
"""a module that request data and save in json format"""
import csv
import json
import requests
from sys import argv


if __name__ == "__main__":
    if argv[1] is None or type(int(argv[1])) is not int:
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
    row = {}
    with open(filename, "w") as f:
        json_list = []
        for thing in things:
            row_dict = {}
            if thing.get("userId", None) == int(argv[1]):
                row_dict["task"] = thing.get("title", None)
                row_dict["completed"] = thing.get("completed", None)
                row_dict["username"] = user.get("username", None)
                json_list.append(row_dict)
        row[str(argv[1])] = json_list
        json.dumps(row)
        f.write(str(row))
