#!/usr/bin/python3
"""Student module"""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of the Student
        If attrs is a list of strings, represents only those attributes
        included in the list
        """
        if not isinstance(attrs, list) or \
           not all(isinstance(i, str) for i in attrs):
            dic = self.__dict__.copy()
        else:
            dic = {i: self.__dict__[i] for i in attrs if i in self.__dict__}

        return (dic)
    
    def reload_from_json(self, json):
        """ replaces all attributes of the Student instance """
        for i in json:
            self.__dict__[i] = json[i]
