#!/usr/bin/python3
"""Model for the BaseModel class"""
import uuid
from datetime import datetime


class BaseModel:
    """
    Parent class of all the rest of serializable classes
    Attributes:
        id (str): unique primary key of the instance
        created_at (datetime): creation time
        updated_at (datetime): update time
    """

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """
        Updates the ``updated_at`` attributes to the current time
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Deserializes the current instance into a dictionary
        Returns:
            a dictionary representing all the instance attributes
        """
        dict = self.__dict__
        dict['__class__'] = self.__class__.__name__
        dict['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        dict['updated_at'] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return dict

    def __str__(self):
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'
