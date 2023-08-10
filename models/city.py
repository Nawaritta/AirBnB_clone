#!/usr/bin/python3
"""Model for the City class"""
from base_model import BaseModel


class City(BaseModel):
    """
    Class which represents a city
    Attributes:
        state_id (str): id of the state where city exists
        name (str): name of the city
    """

    state_id = ''
    name = ''

    def __init__(self):
        pass
