#!/usr/bin/python3
"""Takes in a URL and an email address, sends a POST request to the passed URL
with the email, and finally displays the body of the response."""

from requests import get, post
from sys import argv

if __name__ == "__main__":
    data = {'email': argv[2]}
    response = post(argv[1], data=data)
    print(response.text)
