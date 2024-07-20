#!/usr/bin/python3


def read_file(filename=""):
    # Open the file using the with statement to ensure it's properly closed after reading
    with open(filename, 'r', encoding='utf-8') as file:
        # Read the entire contents of the file
        content = file.read()
        # Print the contents to stdout
        print(content)

# Example usage
read_file("utf-8")
