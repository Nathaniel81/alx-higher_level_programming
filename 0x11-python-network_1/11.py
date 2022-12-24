#!/usr/bin/python3

from sys import argv
from requests import get

result = get("https://api.github.com/repos/{}/{}/commits".format(
    argv[2], argv[1]))
commits = result.json()
print(commits)
