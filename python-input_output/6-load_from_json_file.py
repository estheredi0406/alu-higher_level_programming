#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
A simple utility to load JSON data from a file into a Python object.
"""

import json


def load_from_json_file(filename):
    """
    Reads a JSON file and returns its contents as a Python object (typically a dictionary).

    Parameters:
    - filename (str): The path to the JSON file.

    Returns:
    - dict: The parsed JSON content as a Python dictionary.
    """
    # Open the file using the 'with' statement to ensure proper resource management
    with open(filename, 'r') as file:
        # Read the entire content of the file
        content = file.read()
        
        # Parse the JSON string into a Python object
        obj = json.loads(content)
        
        # Return the parsed object
        return obj
