#!/usr/bin/python3
''' for a given employee id returns information about
employee todo list progress
'''

import requests
from sys import argv


if __name__ == '__main__':
    nameUrl = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    todoUrl = 'https://jsonplaceholder.typicode.com/todos'

    name = requests.get(nameUrl).json().get('name')
    todos = requests.get(todoUrl, params={'userId': int(argv[1])}).json()

    completed = [t.get('title') for t in todos if t.get('completed') is True]

    total = len(todos)
    done = len(completed)

    print('Employee {} is done with tasks({}/{}):'.format(name, done, total))
    [print('\t', complete) for complete in completed]
