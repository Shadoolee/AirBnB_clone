#!/usr/bin/python3
"""Defines the City class, which inherits from the BaseModel."""
from models.base_model import BaseModel

class City(BaseModel):
    """Represents a city.
    Attributes:
        state_id: The ID of the state associated with the city.
        name: The name of the city.
    """
    state_id = ""
    name = ""
