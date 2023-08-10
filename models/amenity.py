#!/usr/bin/python3
"""Model for the Amenity class"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Class which represents amenity
    Attributes:
        name (str): name of the amenity
    """

    name = ''

    def __init__(self):
        super().__init__()
