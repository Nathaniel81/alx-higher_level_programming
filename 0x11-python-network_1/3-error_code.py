#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL and displays
the body of the response (decoded in utf-8)"""

from urllib.request import urlopen
from sys import argv
from urllib.error import HTTPError, URLError

if __name__ == "__main__":
    try:
        with urlopen(argv[1]) as response:
            print(response.read().decode("utf-8"))
    except HTTPError as e:
        print("Error code: {}".format(e.code))
    """except URLError as e:
	    print(e.reason)"""
