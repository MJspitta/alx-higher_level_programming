#!/usr/bin/python3
""" add arguments to a python list and save them to a file """


import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_args_list():
    args = sys.argv[1:]
    try:
        curr_list = load_from_json_file("add_item.json")
    except FileNotFoundError:
        curr_list = []

    new_list = curr_list + args
    save_to_json_file(new_list, "add_item.json")

add_args_list()
