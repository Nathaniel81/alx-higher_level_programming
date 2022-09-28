#!/usr/bin/python3
"""Definition for a python script that adds all arguments to a Python list,
and then save them to a file"""
import sys
import json
from os.path import exists
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

lst = []
if exists(filename):
    lst = load_from_json_file(filename)
lst += sys.argv[1:]
"""print(lst)"""
save_to_json_file(lst, filename)
