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
        Return a dic representation of a student instance """
        return self.__dict__
