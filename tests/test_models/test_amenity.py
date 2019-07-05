#!/usr/bin/python3
"""Module to test Amenity class"""


from models.amenity import Amenity
from tests.test_models.test_base_model import TestBaseModel


class TestAmenity(TestBaseModel):
    """Tests for Amenity class"""

    def setUp(self):
        """Set up which instance to call"""
        self._class = Amenity()
        self._class2 = Amenity()
        self._name = "Amenity"
