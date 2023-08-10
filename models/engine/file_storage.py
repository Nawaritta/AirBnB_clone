#!/usr/bin/python3
""" This module defines the class Filestorage """
import json
from os import path


class FileStorage:
    """ This class serializes instances to a JSON file and deserializes JSON file to instances

    Private class attributes:
    __file_path: string - path to the JSON file (ex: file.json)
    __objects: dictionary - empty but will store all objects by <class name>.id

    Public instance methods:
    all(self): returns the dictionary __objects
    new(self, obj): sets in __objects the obj with key <obj class name>.id
    save(self): serializes __objects to the JSON file (path: __file_path)
    reload(self): deserializes the JSON file to __objects.
    """

    __file_path = 'creatd_instances.json'
    __objects = {}

    def __init__(self):
        pass

    def all(self):
        """
        Returns:

        dict: A dictionary containing all serialized objects.

        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the dictionary of serialized objects.

        Args:
            obj: The object to be added to the dictionary.
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """
        Serializes and saves all objects in the dictionary to the JSON file.
        (path: __file_path)

        """
        serialized = {}
        for key, value in self.__objects.items():
            serialized[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized, file)

    def reload(self):
        """
        deserializes the JSON file to __objects, if the JSON
        file exists, otherwise nothing happens)
        """
        from ..base_model import BaseModel
        from ..user import User
        from ..state import State
        from ..city import City
        from ..amenity import Amenity
        from ..place import Place
        from ..review import Review

        class_dict = {
            'BaseModel': BaseModel,
            'User': User,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review
        }
        if path.exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                if content is not None and content != '':
                    json_dict = json.loads(content)
                for key, value in json_dict.items():
                    obj_class_name = value['__class__']
                    obj_class = class_dict.get(obj_class_name)
                    if obj_class:
                        self.__objects[key] = obj_class(**value)
