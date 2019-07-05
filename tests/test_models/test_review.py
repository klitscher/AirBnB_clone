#!/usr/bin/python3
"""Module to test Review class"""


from models.review import Review
from tests.test_models.test_base_model import TestBaseModel


class TestReview(TestBaseModel):
    """Tests for BaseModel class"""

    def setUp(self):
        """Set up which instance to call"""
        self._class = Review()
        self._class2 = Review()
        self._name = "Review"
