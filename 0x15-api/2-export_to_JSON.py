#!/usr/bin/python3
''' for a given employee id returns information about
employee todo list progress
'''

import json
import requests
from sys import argv


if __name__ == '__main__':
    nameUrl = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    todoUrl = 'https://jsonplaceholder.typicode.com/todos'

    user = requests.get(nameUrl).json().get('username')
    todos = requests.get(todoUrl, params={'userId': int(argv[1])}).json()

    data = [{'task': todo.get('title'),
             "completed": todo.get('completed'),
             "username": user} for todo in todos]

    jsonData = {argv[1]: data}

    with open(argv[1] + '.json', 'w') as f:
        json.dump(jsonData, f)
