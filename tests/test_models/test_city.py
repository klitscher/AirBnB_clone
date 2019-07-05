#!/usr/bin/python3
"""Module to test City class"""


from models.city import City
from tests.test_models.test_base_model import TestBaseModel


class TestCity(TestBaseModel):
    """Tests for City class"""

    def setUp(self):
        """Set up which instance to call"""
        self._class = City()
        self._class2 = City()
        self._name = "City"
