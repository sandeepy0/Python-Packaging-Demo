#!/usr/bin/python3

import os
from sys import path as sys_path
import pkg_resources

resource_path = "resources/DORAEMON"
doraemon_path = pkg_resources.resource_filename(__name__, resource_path)

def bubble(message):
    bubble_length = len(message) + 3
    return f"""
 {"_" * bubble_length}
( {message} )
 {"‾" * bubble_length}"""

def fetch_message(path):
    """Read text file and return its contents."""
    cwd = os.getcwd()
    print(f"cwd: {cwd}")
    print(f"sys_path: {sys_path}")
    with open(path) as f:
        return f.read()

def say(message):
    DORAEMON = fetch_message(doraemon_path)
    message = "Hello Guys, I am doraemon. " +  message
    print(bubble(message))
    print(DORAEMON)
