#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status
using the request package"""

import requests

if __name__ == '__main__':
    response = requests.get('https://alx-intranet.hbtn.io/status').text
    print("Body response:")
    print("\t- type: {}".format(type(response)))
    print("\t- content: {}".format(response))
