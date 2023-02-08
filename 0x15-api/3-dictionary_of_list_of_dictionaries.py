#!/usr/bin/python3
''' for a given employee id returns information about
employee todo list progress
'''

import json
import requests
from sys import argv


if __name__ == '__main__':
    nameUrl = 'https://jsonplaceholder.typicode.com/users'
    todoUrl = 'https://jsonplaceholder.typicode.com/todos'

    users = requests.get(nameUrl).json()
    allTodos = requests.get(todoUrl).json()
    totalUsers = len(users)

    jsonData = {}
    for userId in range(1, totalUsers + 1):
        user = users[userId - 1].get('username')
        data = [{'task': todo.get('title'),
                "completed": todo.get('completed'),
                 "username": user} for todo in allTodos
                if userId == todo.get('userId')]
        jsonData[userId] = data

    with open('todo_all_employees.json', 'w') as f:
        json.dump(jsonData, f)
