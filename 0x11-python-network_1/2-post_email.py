#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""

from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv

if __name__ == '__main__':
    data = {'email': argv[2]}
    reqObj = urlencode(data).encode('ascii')
    req = Request(argv[1], data=reqObj, method='POST')
    with urlopen(req) as response:
        print(response.read().decode('utf-8'))
