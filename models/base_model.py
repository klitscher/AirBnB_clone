#!/usr/bin/python3
"""Defines the BaseModel class."""


import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel for all BnB project"""

    def __init__(self, *args, **kwargs):
        """Initializes a new BaseModel:

        Args:
            *args: Unused for now.
            **Kwargs: Key/values of pairs of attributes.
        """
        timeDisplay = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if len(kwargs) != 0:
            for value1, value2 in kwargs.items():
                if value1 is "created_at" or value1 is "updated_at":
                    self.__dict__[value1] = datetime.strptime(value2,
                                                              timeDisplay)
                else:
                    self.__dict__[value1] = value2

    def save(self):
        """Saves updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Updates dictionary and returns BaseModel instance.

        returns class name of object
        value key/pair included
        """
        UpdateDictionary = self.__dict__.copy()
        UpdateDictionary["updated_at"] = datetime.isoformat((self.updated_at))
        UpdateDictionary["created_at"] = datetime.isoformat((self.created_at))
        UpdateDictionary["__class__"] = self.__class__.__name__
        return UpdateDictionary

    def __str__(self):
        """Returns the print str of BaseModel instance"""

        ClassName = self.__class__.__name__
        return "[{}] ({}) {}" .format(ClassName, self.id, self.__dict__)
