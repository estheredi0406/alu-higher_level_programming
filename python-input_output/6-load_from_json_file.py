#!/usr/bin/env python3
# This script loads a Python object from a JSON file


import json


def load_from_json_file(filename):
    """
    Reads a JSON file and returns the corresponding Python object.
    
    Parameters:
        filename (str): The name of the JSON file to read.
        
    Returns:
        Any: The Python object represented by the JSON file content.
    """
    # Open the file in read mode ('r') with UTF-8 encoding
    with open(filename, 'r', encoding='utf-8') as file:
        # Parse the JSON file content into a Python object
        return json.load(file)
