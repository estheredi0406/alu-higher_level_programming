#!/usr/bin/python3


"""
Defines a Student class with attributes for first_name, last_name, and age.
Includes a method to_json for serializing the instance into a dictionary, optionally filtering attributes.
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

        """
    Retrives a dic reprsentation of the student instance.
    """
    
    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance, optionally filtering attributes.
        
        Parameters:
        - attrs (list[str], optional): List of attribute names to include in the output. Defaults to None, meaning all attributes are included.
        
        Returns:
        - dict: A dictionary representing the student's information, filtered by the provided attribute names.
        """
        try:
            for attr in attrs:
                if type(attr) is not str:
                    return self.__dict__
        except Exception:
            return self.__dict__
        my_dict = dict()
        for key, value in self.__dict__.items():
            if key in attrs:
                my_dict[key] = value
        return my_dict

