#!/usr/bin/python3
#another one

"""
    Converts an instance of a class into a JSON-compatible dictionary.

    Parameters:
    - obj: An instance of a class whose attributes are serializable (list, dictionary, string, integer, boolean).

    Returns:
    - dict: A dictionary representing the object's state, ready for JSON serialization.
    """


def class_to_json(obj):
    """
    Converts an instance of a class into a JSON-compatible dictionary.

    """

    result = {}

    # Check if obj is an instance of a custom class
    if hasattr(obj, '__dict__'):
        # Convert the object's attributes to a dictionary
        for attr_name, attr_value in obj.__dict__.items():
            # Skip private variables (those starting with double underscores)
            if attr_name.startswith('__'):
                continue

            # Recursively convert nested objects
            if isinstance(attr_value, (list, dict, str, int, bool)):
                result[attr_name] = attr_value
            else:
                # Handle nested objects by calling the function recursively
                result[attr_name] = class_to_json(attr_value)

    return result
