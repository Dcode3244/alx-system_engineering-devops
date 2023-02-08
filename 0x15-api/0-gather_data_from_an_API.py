#!/usr/bin/python3
''' for a given employee id returns information about
employee todo list progress
'''

if __name__ == '__main__':
    import requests
    from sys import argv

    nameUrl = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    todoUrl = 'https://jsonplaceholder.typicode.com/todos'

    name = requests.get(nameUrl).json().get('name')
    todos = requests.get(todoUrl, params={'userId': int(argv[1])}).json()

    total = len(todos)
    done = 0

    for todo in todos:
        if todo.get('completed') is True:
            done += 1

    print('Employee {} is done with tasks({}/{}):'.format(name, done, total))
    for todo in todos:
        if todo.get('completed') is True:
            print('\t', todo.get("title"))
