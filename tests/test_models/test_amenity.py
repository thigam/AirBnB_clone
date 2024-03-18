#!/usr/bin/python3
from models.base_model import BaseModel
from models.__init__ import storage
import unittest

class TestAmenity(unittest.TestCase):
    def test_init(self):
        """Checks whether the init method creates an instance of Amenity"""
        new=Amenity()
        self.assertIsInstance(new, Amenity)

    def test_to_str(self):
        """Checks whether the output of to_str is according to the desired format"""
        new=Amenity()
        self.assertEqual(new.__str__(), "[{}] ({}) {}".format(new.__class__.__name__, new.id, new.__dict__))

    def test_to_dict(self):
        """Checks whether the to_dict method adds the __class__ key"""
        new = Amenity()
        self.assertIn("__class__", new.to_dict())

