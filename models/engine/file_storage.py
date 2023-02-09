#!/usr/bin/python3
""""
serializes instances to a JSON file and deserializes JSON file to instances
"""

import json
from os import path
from models.base_model import BaseModel


class FileStorage:
    """
    serializes instances to a JSON file and deserializes JSON file to instances
    """
    
    def __init__(self):
        """
        initialise attributes
        """
        self.__file_path = 'file.json'
        self.__objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return self.__objects
    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        """
        serialises objects into a json file(path: __file_path)
        """
        json_dict = {}

        for k, v in self.__objects.items():
            json_dict[k] = v.to_dict()
        with open(self.__file_path, mode = 'w', encoding = 'utf-8') as f:
            f.write(json.dumps(json_dict))

    def reload(self):
        """
        deserialises the json file __file_path 
        and raises no exception if file does not exist
        """

        if path.exists(self.__file_path):
            with open(self.__file_path, mode = 'r', encoding = 'utf-8') as f:
                json_dict = json.loads(f.read())
            for k, v in json_dict.items():
                self.__objects[k] = eval(v['__class__'])(**v)

            

