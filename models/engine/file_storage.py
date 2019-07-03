#!/usr/bin/python3
"""Module to create a file storage system"""


import json
from os.path import isfile


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
        """Sets in __object the obj with key <obj class name>.id

        Args:
            obj - instance that is passsed in
        """
        key = '{}.{}'.format(obj.__class__.__name__, obj.id)
        value = obj.to_dict()
        type(self).__objects[key] = value

    def save(self):
        """Serializes __objects to the JSON file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        dic = type(self).__objects.copy()
        with open(type(self).__file_path, 'w+') as f:
            for key, value in dic.items():
                if isinstance(value, BaseModel):
                    value2 = value.to_dict()
                    type(self).__objects[key] = value2
                if isinstance(value, User):
                    value2 = value.to_dict()
                    type(self).__objects[key] = value2
                if isinstance(value, State):
                    value2 = value.to_dict()
                    type(self).__objects[key] = value2
                if isinstance(value, City):
                    value2 = value.to_dict()
                    type(self).__objects[key] = value2
                if isinstance(value, Amenity):
                    value2 = value.to_dict()
                    type(self).__objects[key] = value2
                if isinstance(value, Place):
                    value2 = value.to_dict()
                    type(self).__objects[key] = value2
                if isinstance(value, Review):
                    value2 = value.to_dict()
                    type(self).__objects[key] = value2
            json.dump(type(self).__objects, f)

    def reload(self):
        """Deserializes the Json file to __objects if the file exists"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        dic = {}
        dic2 = {}
        if isfile(type(self).__file_path):
            with open(type(self).__file_path, 'r') as f:
                dic = json.load(f)
                for key, value in dic.items():
                    dic2 = value
                    if dic2['__class__'] == 'BaseModel':
                        instance = BaseModel(**dic2)
                    if dic2['__class__'] == 'User':
                        instance = User(**dic2)
                    if dic2['__class__'] == 'State':
                        instance = State(**dic2)
                    if dic2['__class__'] == 'City':
                        instance = City(**dic2)
                    if dic2['__class__'] == 'Amenity':
                        instance = Amenity(**dic2)
                    if dic2['__class__'] == 'Place':
                        instance = Place(**dic2)
                    if dic2['__class__'] == 'Review':
                        instance = Review(**dic2)
                    dic[key] = instance
                type(self).__objects = dic
