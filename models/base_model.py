#!/usr/bin/python3

"""
A module containing the definition for the base class that defines all common attributes/methods for other classes
"""
import uuid
from datetime import datetime
from .__init__ import storage


class BaseModel:
    """The base class that contains all common attributes/methods for other classes"""
    def __init__(self, *args, **kwargs):
        """The initialization method for new instances"""
        if kwargs:
            for key,value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    self.key = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.key = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """The custom __str__ called upon using the print() function"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """The save function that saves to a file"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """A function that customizes the output of __dict__ attribute"""
        custom_dictionary = {}
        for key, value in self.__dict__.items():
            if value is None:
                continue
            if key == "created_at" or key == "updated_at":
                value = value.isoformat()
            custom_dictionary[key] = value
        custom_dictionary["__class__"] = self.__class__.__name__
        return custom_dictionary
