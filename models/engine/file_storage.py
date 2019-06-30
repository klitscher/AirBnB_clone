#!/usr/bin/python3
"""Module to create a file storage system"""


import json
from os.path import isfile
from collections import namedtuple


class FileStorage:
    """Class for serializeing and deserializing python obects

    __file_path: string - path to JSON file
    __objects: dictionary - empty but will store all objects by <class name>.id
    """

    __file_path = 'instance.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return type(self).__objects

    def new(self, obj):
        """Sets in __object the obj with key <obj class name>.id"""
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        value = obj.to_dict()
        type(self).__objects[key] = value

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(type(self).__file_path, 'w+') as f:
            json.dump(type(self).__objects, f)

    def reload(self):
        """Deserializes the Json file to __objects if the file exists"""
        dic = {}
        from models.base_model import BaseModel
        if isfile(type(self).__file_path):
            with open(type(self).__file_path, 'r') as f:
                dic = json.load(f)
                for key, value in dic.items():
                    print(value)
#                FileStorage.__objects = json.load(f)

