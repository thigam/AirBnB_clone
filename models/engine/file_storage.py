#!/usr/bin/python3
import os
import json

class FileStorage:
    """Deals with the storage of dictionary representations of baseModel objects in a json file"""
    __file_path = "models/file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects which is a private class attribute"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key as the classname.id"""
        FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj.to_dict()

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, "w") as json_file:
            json.dump(FileStorage.__objects, json_file)

    def update(self, obj):
        """Updates the objects in __objects before the save method of FileStorage is called"""
        if obj.__class__.__name__ == "User":
            FileStorage.__objects["{}.{}".format(obj.__class__.__name__, obj.id)] = obj.to_dict()

    def reload(self):
        """DEserializes the JSON file to __objects only if it exists"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as json_file:
                try:
                    FileStorage.__objects = json.load(json_file)
                except:
                    pass
                """
                full_list = json_file.read()
                json_objs = full_list.split(', "BaseModel.')
                if len(json_objs) == 1:
                    json_object = json.loads(full_list)
                    FileStorage.__objects.update(json_object)
                else:
                    for counter, json_string in enumerate(json_objs):
                        if counter > 0:
                            json_string = '"BaseModel.' + json_string.strip()
                        json_object = json.loads(json_string)
                        FileStorage.__objects.update(json_object)
                        """
