#!/usr/bin/python3
"""Module to test FileStorage class"""

from models import storage
from models.base_model import BaseModel
from datetime import datetime, timedelta
import unittest
import io
from models.base_model import BaseModel
from contextlib import redirect_stdout
from time import sleep


class TestFileStorage(unittest.TestCase):
    """Tests for FileStorage class"""

    # ------------General Tests------------------------------------------------

    # ------------Test all method-----------------------------------------------

    def test_Correct(self):
        """Tests correct output"""
        self.assertRaises(TypeError, storage.all, "Test")
