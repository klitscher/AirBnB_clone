#!/usr/bin/python3
"""Defines the BaseModel class."""


from os.path import isfile
from models import storage
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
        if len(kwargs) == 0:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            kwargs.pop('__class__')
            for key, value in kwargs.items():
                if key is "created_at" or key is "updated_at":
                    self.__dict__[key] = datetime.strptime(value,
                                                           timeDisplay)
                else:
                    setattr(self, key, value)

    def save(self):
        """Saves updated_at with the current datetime"""
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Updates dictionary and returns BaseModel instance.

        returns class name of object
        value key/pair included
        """
        timeDisplay = "%Y-%m-%dT%H:%M:%S.%f"
        UpdateDictionary = self.__dict__.copy()
        if (type(self.updated_at)) is str:
            self.updated_at = datetime.strptime(self.updated_at, timeDisplay)
        if (type(self.created_at)) is str:
            self.created_at = datetime.strptime(self.created_at, timeDisplay)
        UpdateDictionary["updated_at"] = datetime.isoformat((self.updated_at))
        UpdateDictionary["created_at"] = datetime.isoformat((self.created_at))
        UpdateDictionary["__class__"] = self.__class__.__name__
        return UpdateDictionary

    def __str__(self):
        """Returns the print str of BaseModel instance"""

        ClassName = self.__class__.__name__
        return "[{}] ({}) {}" .format(ClassName, self.id, self.__dict__)
