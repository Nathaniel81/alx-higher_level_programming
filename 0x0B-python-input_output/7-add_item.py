#!/usr/bin/python3
"""Defining a python script"""
import sys
import json
from os.path import exists
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

"""with open(filename, "a+", encoding="utf-8") as myFile:
    save_to_json_file(sys.argv[1:], filename)
    load_from_json_file(filename)"""
lst = []
if exists(filename):
    lst = load_from_json_file(filename)
lst += sys.argv[1:]

save_to_json_file(lst, filename)
