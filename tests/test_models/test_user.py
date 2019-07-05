#!/usr/bin/python3
"""Module to test User class"""



from models.user import User
from tests.test_models.test_base_model import TestBaseModel


class TestUser(TestBaseModel):
    """Tests for User class"""

    def setUp(self):
        """Set up which instance to call"""
        self._class = User()
        self._class2 = User()
        self._name = "User"
