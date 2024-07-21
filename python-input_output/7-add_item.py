#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
This script collects command-line arguments, stores them in a Python list,
and saves this list to a file named 'add_item.json'. It utilizes functions
from '5-save_to_json_file.py' and '6-load_from_json_file.py'.
"""

import sys
from 5_save_to_json_file import save_to_json_file
from 6_load_from_json_file import load_from_json_file


def main():
    """
    Main function to execute the script's functionality.
    Collects command-line arguments, stores them in a list, and saves this list to a file.
    """
    # Initialize an empty list to store command-line arguments
    args_list = []
    
    # Iterate over command-line arguments starting from index 1 (0 is the script name)
    for arg in sys.argv[1:]:
        args_list.append(arg)
    
    # Save the list to a file named "add_item.json"
    save_to_json_file("add_item.json", args_list)
    
    # Load the list from the file to verify
    loaded_list = load_from_json_file("add_item.json")
    print(f"Loaded list: {loaded_list}")

if __name__ == "__main__":
    main()

