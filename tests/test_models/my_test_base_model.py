#!/usr/bin/python3
from models.base_model import BaseModel
import unittest

class TestBaseModel(unittest.TestCase):
    def test_init(self):
        new=BaseModel()
        self.assertIsInstance(new, BaseModel)

    def test_to_dict(self):
        new=BaseModel()
        self.assertEqual(new.__str__(), "[{}] ({}) {}".format(new.__class__.__name__, new.id, new.__dict__))

