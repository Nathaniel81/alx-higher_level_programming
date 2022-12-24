#!/usr/bin/python3
""" list 10 commits (from the most recent to oldest)
of the repository 'rails' by the user 'rails' """

from sys import argv
from requests import get

if __name__ == "__main__":
    result = get("https://api.github.com/repos/{}/{}/commits".format(
        argv[2], argv[1]))
    commits = result.json()
    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get("sha"),
                commits[i].get("commit").get("author").get("name")))
    except IndexError:
        pass
