#!/usr/bin/python3
"""
This module demonstrates how to collect command-line
arguments, combine them with existing items from a JSON file,
and save the updated list back to the file.
It showcases the use of JSON serialization and deserialization in Python.
"""


import sys
import json


# Assuming the existence of these functions from previous exercises
# def save_to_json_file(my_obj, filename)
# def load_from_json_file(filename)


def load_from_json_file(filename):
    """
    Loads a JSON file and returns the corresponding Python object.
    
    Args:
        filename (str): The path to the JSON file.
        
    Returns:
        Any: The Python object loaded from the JSON file.
    """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)

def save_to_json_file(my_obj, filename):
    """
    Saves a Python object to a JSON file.
    
    Args:
        my_obj (Any): The Python object to serialize.
        filename (str): The path to the JSON file where
        the object will be saved.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file, ensure_ascii=False, indent=4)

def main():
    # Initialize an empty list to collect command-line arguments
    args_list = []
    
    # Collect all command-line arguments excluding the script name
    args_list.extend(sys.argv[1:])
    
    # Attempt to load existing items from the JSON file
    try:
        existing_items = load_from_json_file('add_item.json')
    except FileNotFoundError:
        existing_items = []
    
    # Combine the existing items with the new arguments
    combined_items = existing_items + args_list
    
    # Save the combined list back to the JSON file
    save_to_json_file(combined_items, 'add_item.json')

if __name__ == "__main__":
    main()

