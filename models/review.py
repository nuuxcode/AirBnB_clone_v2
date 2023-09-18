#!/usr/bin/python3
""" Review module for the HBNB project """
from models.base_model import BaseModel, Base
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")


class Review(BaseModel, Base):
    """ Review classto store review information """
    __tablename__ = 'reviews'

    if storage_type == "db":
        pass  # review code
    else:
        place_id = ""
        user_id = ""
        text = ""
