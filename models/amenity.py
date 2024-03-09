#!/usr/bin/python3
"""Contains the definition for a class User that inherits from BaseModel"""
from .base_model import BaseModel

class Amenity(BaseModel):
    """A class that holds information about the available amenities"""
    name = ""
