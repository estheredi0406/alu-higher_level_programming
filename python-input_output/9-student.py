#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
Defines a Student class with attributes for first_name, last_name, and age.
Includes a method to_json for serializing the instance into a JSON-compatible dictionary.
"""


class Student:
    """
    Represents a student with attributes for first_name, last_name, and age.
    """
    
    def __init__(self, first_name, last_name, age):
        """
        Initializes a new instance of the Student class.
        
        Parameters:
        - first_name (str): The student's first name.
        - last_name (str): The student's last name.
        - age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self):
        """
        Retrieves a dictionary representation of the Student instance.
        
        Returns:
        - dict: A dictionary representing the student's information.
        """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }

# Example usage
student_instance = Student('John', 'Doe', 22)
print(student_instance.to_json())
