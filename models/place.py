#!/usr/bin/python3
"""Place class module"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class
    Attributes:
        city_id (str): the city id
        user_id (str): the user id
        name (str): the name of the place
        description (str): the description of the place
        number_rooms (int): the number of rooms
        number_bathrooms (int): the number of bathrooms
        max_guest (int): the max number of guests
        price_by_night (int): the price by night
        latitude (float): the latitude of the place
        longitude (float): the longitude of the place
        amenity_ids (list): list of amenity ids
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
