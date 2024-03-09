#!/usr/bin/python3
"""Contains the definition for a class User that inherits from BaseModel"""
from .base_model import BaseModel

class Place(BaseModel):
    """Holds a description of the place including specific details"""
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_nght = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
