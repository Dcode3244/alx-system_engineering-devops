#!/usr/bin/python3
''' for a given employee id returns information about
employee todo list progress
'''

import csv
import requests
from sys import argv


if __name__ == '__main__':
    nameUrl = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    todoUrl = 'https://jsonplaceholder.typicode.com/todos'

    user = requests.get(nameUrl).json().get('username')
    todos = requests.get(todoUrl, params={'userId': int(argv[1])}).json()

    data = [[argv[1], user, t.get('completed'), t.get('title')] for t in todos]

    with open('exp.csv', 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        [writer.writerow(d) for d in data]
