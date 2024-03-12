#!/usr/bin/python3

import os
from os.path import exists
from json import dump, load
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.user import User
from models.state import State

class FileStorage:
    __file_path = 'file.json'
    __objects = {}
    class_dict = {
        "BaseModel": BaseModel,
        "City": City,
        "State": State,
        "User": User,
        "Amenity": Amenity
    }

    def all(self):
        """Return private attribute __objects in dictionary format."""
        return self.__objects

    def new(self, obj):
        """Add a new object to __objects."""
        class_name = obj.__class__.__name__
        class_id = obj.id
        key = class_name + "." + class_id
        self.__objects[key] = obj

    def save(self):
        """Serialize __objects into a JSON file."""
        serialized_objects = {key: value.to_dict() for key, value in self.__objects.items()}
        with open(self.__file_path, 'w') as file:
            dump(serialized_objects, file)

    def reload(self):
        """
        Deserialize the JSON file to __objects.
        If the file doesn't exist, do nothing.
        """
        try:
            with open(self.__file_path, 'r') as file:
                data = load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    new_obj = self.class_dict[class_name](**value)
                    self.__objects[key] = new_obj

        except Exception:
            pass
