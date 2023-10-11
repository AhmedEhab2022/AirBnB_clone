#!/usr/bin/python3
"""City class module"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class
    Attributes:
        state_id (str): the state id
        name (str): the name of the city
    """
    state_id = ""
    name = ""
