#!/usr/bin/python3
"""Model for the State class"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    Class which represents a state
    Attributes:
        name (str): name of the state
    """

    name = ''

    def __init__(self):
        super().__init__()
