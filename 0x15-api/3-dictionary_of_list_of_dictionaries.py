#!/usr/bin/python3
"""a module that request data and save in json format"""
import requests
from sys import argv
import csv
import json


if __name__ == "__main__":
    filename = "todo_all_employees.json"
    url = "https://jsonplaceholder.typicode.com"
    try:
        res_user = requests.get(url + "/users/")
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
        for u_id in user:
            json_list = []
            for thing in things:
                row_dict = {}
                if thing["userId"] == u_id["id"]:
                    row_dict["username"] = u_id["username"]
                    row_dict["task"] = thing["title"]
                    row_dict["completed"] = thing["completed"]
                    json_list.append(row_dict)
            row[u_id["id"]] = json_list
        json.dumps(row)
        f.write(str(row))
