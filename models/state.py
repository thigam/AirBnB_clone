#!/usr/bin/python3
"""Contains the definition for a class User that inherits from BaseModel"""
from .base_model import BaseModel

class State(BaseModel):
    """A class that represents the state of the individual"""
    name = ""
