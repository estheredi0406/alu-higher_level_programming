#!/usr/bin/python3
"""defining to_json_string"""


import json

def save_to_json_file(my_obj, filename):
    """
    Saves a Python object to a text file using its
    JSON representation.
    
    Parameters:
        my_obj: The Python object to serialize and save.
        filename (str): The name of the file where the
        JSON representation will be saved.
    """
    # Open the file in write mode ('w') with UTF-8 encoding
    with open(filename, 'w', encoding='utf-8') as file:
        # Serialize the Python object to a JSON-formatted
        # string and write it to the file
        json.dump(my_obj, file, ensure_ascii=False, indent=4)
