#!/usr/bin/python3
"""defining to_json_string"""


import json


def from_json_string(my_str):
    """
    Converts a JSON string into a Python object.

    Parameters:
        my_str (str): The JSON string to convert.

    Returns:
        Any: The Python object represented by the JSON string.
    """
    return json.loads(my_str)
