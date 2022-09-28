#!/usr/bin/python3
"""Defining load_from_json_file function"""
import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file"""

    with open(filename, "r", encoding="utf-8") as myFile:
        return json.load(myFile)
