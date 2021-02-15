#!/usr/bin/python3
"""place class, inherits base"""


from models.base_model import BaseModel


class Place(BaseModel):
    """a class named User template that inherits from BaseModel"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0.0
    latitue: 0.0
    longitude = 0.0
    amenity_ids = []
