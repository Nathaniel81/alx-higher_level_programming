#!/usr/bin/python3
"""Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""

from requests import post
from sys import argv

if __name__ == "__main__":
    data = {"q": "" if len(argv) == 1 else argv[1]}
    response = post("http://0.0.0.0:5000/search_user", data=data)
    try:
        jsonRsp = response.json()
        if jsonRsp == {}:
            print("No result")
        else:
            print(f"[{jsonRsp.get(id)}] {jsonRsp.get('name')}")
    except ValueError:
        print("Not a valid JSON")
