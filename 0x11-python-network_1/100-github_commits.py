#!/usr/bin/python3
"""Write a Python script that takes 2 arguments in order to solve challenge
"""

import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    user = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(user, repo_name)
    req = requests.get(url)
    commits = req.json()
    for c in commits[:10]:
        print(c.get('sha'), end=': ')
        print(c.get('commit').get('author').get('name'))
