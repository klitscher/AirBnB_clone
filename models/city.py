#!/usr/bin/python3
"""Defines the City class."""


from models.base_model import BaseModel


class City(BaseModel):
    """City class for AirBnB project

    state_id - empty string: it will be the State.id
    name - empty string
    """

    state_id = ""
    name = ""
