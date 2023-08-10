#!/usr/bin/python3
"""Model for the Place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Class which represents a place
    Attributes:
        city_id (str): id of the city of the place
        user_id (str): id of the user renting the place
        name (stt): name of the place
        description (str): description of the place
        number_rooms (int): number of rooms in the place
        number_bathrooms (int): number of bathrooms in the place
        max_guest (int): maximum number of guest that can be brough
        price_by_night (int): price per night id stay
        latitude (float): longitude of the place's location
        longitude (float): latitude of the place's location
        amenity_ids (list[str]): list if amenity ids the around the place
    """

    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
