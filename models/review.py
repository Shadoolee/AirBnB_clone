#!/usr/bin/python3
"""Defines the Review class, which inherits from the BaseModel."""
from models.base_model import BaseModel

class Review(BaseModel):
    """Represents a review object with various attributes."""
    place_id = ""
    user_id = ""
    text = ""
