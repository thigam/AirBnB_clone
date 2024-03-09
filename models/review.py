#!/usr/bin/python3
"""Contains the definition for a class User that inherits from BaseModel"""
from .base_model import BaseModel

class Review(BaseModel):
    """A class that gives rise to indivudal reviews about a particular place"""
    place_id = ""
    user_id = ""
    text = ""
