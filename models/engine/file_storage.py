#!/usr/bin/python3
"""This is the file storage class for AirBnB"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """This class serializes instances to a JSON file and
    deserializes JSON file to instances
    Attributes:
        __file_path: path to the JSON file
        __objects: objects will be stored
    """
    __file_path = "file.json"
    __objects = {}

    def close(self):
        self.reload()

    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
            v2. return objects for a specific class
        """
        dic = {}
        ob = self.__objects
        if cls:
            # print('file_storage - cls given')
            for i in ob.keys():
                # print("from file_storage --> k:{} v:{}".format(i, ob[i]))
                objects = ob[i]
                # print(type(objects))
                # print(cls)
                if type(objects) is cls:
                    # print("instance found!!")
                    dic[i] = ob[i]
            # print("dic ->>>>>>|>>>", dic)
            return dic
        return ob

    def new(self, obj):
        """sets __object to given obj
        Args:
            obj: given object
        """
        if obj:
            key = "{}.{}".format(type(obj).__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serialize the file path to JSON file path
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """serialize the file path to JSON file path
        """
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """delete obj from __objects if it’s inside
        """
        ob = self.__objects

        for k, v in ob.items():
            if obj is v:
                del self.__objects[k]
                self.save()
                return

    def close(self):
        """calls reload"""
        self.reload()
