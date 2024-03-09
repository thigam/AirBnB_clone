#!/usr/bin/python3
"""Contains the definition for a class User that inherits from BaseModel"""
from .base_model import BaseModel

class City(BaseModel):
    """Holds information about the individual's city"""
    state_id = ""
    name = ""
