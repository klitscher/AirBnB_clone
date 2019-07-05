#!/usr/bin/python3
"""Module to test Place class"""


from models.place import Place
from tests.test_models.test_base_model import TestBaseModel


class TestPlace(TestBaseModel):
    """Tests for BaseModel class"""

    def setUp(self):
        """Set up which instance to call"""
        self._class = Place()
        self._class2 = Place()
        self._name = "Place"
