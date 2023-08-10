#!/usr/bin/python3
"""Model for the User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Class which represents a user
    Attributes:
        email (str): email of the user
        password (str): password of the user
        first_name (str): first_name of the user
        last_name (str): last_name of the user
    """

    email = ''
    password = ''
    first_name = ''
    last_name = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
