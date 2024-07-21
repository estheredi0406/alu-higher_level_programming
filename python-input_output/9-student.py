#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Defines a Student class with attributes for first_name, last_name, and age.
Includes a method to_json for serializing the instance into a formatted string representation.
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
        Retrieves a formatted string representation of the Student instance.
        
        Returns:
        - str: A formatted string representing the student's information.
        """
        result = []
        for key, value in self.__dict__.items():
            result.append(f"{key} => {value} / <class '{type(value).__name__}'>")
        return "\n".join(result)

# Example usage
student_instance = Student('Tom', 'Smith', 89)
formatted_output = student_instance.to_json()
print(formatted_output)
