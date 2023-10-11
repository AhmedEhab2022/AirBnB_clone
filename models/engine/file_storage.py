#!/usr/bin/python3
"""FileStorage class module"""

import json
import os


class FileStorage():
    """
    FileStorage class
    Attributes:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    Methods:
        all(self)
        new(self, obj)
        save(self)
        reload(self)
    """

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Initializes the instance"""
        pass

    def all(self):
        """Returns the dictionary representation of __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        FileStorage.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, "w") as file:
            storage_dict = {k: v.to_dict()
                            for k, v in FileStorage.__objects.items()}
            json.dump(storage_dict, file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if not os.path.exists(FileStorage.__file_path):
            return

        with open(FileStorage.__file_path, "r") as f:
            strorage_dict = json.load(f)
            for v in strorage_dict.values():
                cls = v["__class__"]
                self.new(self.classes()[cls](**v))

    def classes(self):
        """Map class names to python classes"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review

        }

        return classes
