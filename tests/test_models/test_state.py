#!/usr/bin/python3
"""Module to test State class"""


from models.state import State
from tests.test_models.test_base_model import TestBaseModel


class TestState(TestBaseModel):
    """Tests for State class"""

    def setUp(self):
        """Set up which instance to call"""
        self._class = State()
        self._class2 = State()
        self._name = "State"
