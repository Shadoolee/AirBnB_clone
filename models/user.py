#!/usr/bin/python3
"""Defines the User class, which inherits from the BaseModel."""
from models.base_model import BaseModel

class User(BaseModel):
    """Represents a user object with various attributes."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
