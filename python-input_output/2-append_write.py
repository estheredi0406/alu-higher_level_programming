#!/usr/bin/python3
"""defining the function"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a file,
    creating the file if it doesn't exist.

    Parameters:
        filename (str): The name of the file to append to.
        text (str): The text to append to the file.

    Returns:
        int: The number of characters appended.
    """
    # Open the file in append mode ('a') with UTF-8 encoding
    with open(filename, "a", encoding='utf-8') as file:
        # Write the text to the file and return
        # the number of characters written
        return file.write(text)
