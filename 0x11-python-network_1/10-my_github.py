#!/usr/bin/python3
"""Takes GitHub credentials (username and password)
and uses the GitHub API to display an id"""

from requests import get, auth
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    response = get("https://api.github.com/user", auth=(username, password))
    data = response.json()
    print(data.get('id'))
