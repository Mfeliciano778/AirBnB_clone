#!/usr/bin/python3
"""
Manages the storage of JSON strings for all class instances
"""

import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review

# list or dictionary for case validation (need to add pattern of dict)
a_dict = {}

class FileStorage:
    """ Serializes and deserializes object instances to JSON files """

    __file_path = "file.json"
    __objects = {}

    

    def all(self):
        """ Returns the dictionary __objects """

    def new(self, obj):
        """  sets in __objects the obj with key <obj class name>.id """

    def save(self):
    """ Serializes __objects to the JSON file (path: __file_path) """
    with open(filename, 'w', encoding='utf-8') as myfile:
        json.dump(my_obj, myfile)

    def reload(self):
        """  deserializes the JSON file to __objects """
        # (only if the JSON file (__file_path) exists
        # otherwise, do nothing. 
        # If the file doesn’t exist, no exception should be raised)