#!/usr/bin/python3
"""Model for the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Class which represents a review
    Attributes:
        place_id (str): place which the review is about
        user_id (str): the user makibg the review
        text (str): text of actual review
    """

    place_id = ''
    user_id = ''
    text = ''

    def __init__(self):
        super().__init__()
