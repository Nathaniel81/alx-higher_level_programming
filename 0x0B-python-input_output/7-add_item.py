#!/usr/bin/python3
"""Defining a python script"""
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

with open(filename, "a+", encoding="utf-8") as myFile:
    save_to_json_file(sys.argv[1:], filename)
    load_from_json_file(filename)
