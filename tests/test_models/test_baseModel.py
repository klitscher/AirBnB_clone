#!/usr/bin/python3
"""Module to test BaseModel class"""


from datetime import datetime, timedelta
import unittest
import io
from models.base_model import BaseModel
from contextlib import redirect_stdout
from time import sleep


class TestBaseModel(unittest.TestCase):
    """Tests for BaseModel class"""

    # -------------Tests Public Attributes--------------------------------------

    def test_idCorrect(self):
        """Test that id is a unique string"""
        my_model1 = BaseModel()
        my_model2 = BaseModel()
        self.assertTrue((type(my_model1.id) is str))
        self.assertNotEqual(my_model1.id, my_model2.id)

    def test_createUpdateType(self):
        """Test that create and update are datetime objects"""
        my_model = BaseModel()
        self.assertTrue(isinstance(my_model.created_at, datetime))
        self.assertTrue(isinstance(my_model.updated_at, datetime))

    def test_updateDif(self):
        """Test that update is different than create after update"""
        my_model = BaseModel()
        t1 = my_model.created_at - my_model.updated_at
        self.assertTrue((t1.total_seconds() * -1000000) < 100)
        my_model.name = "Holberton"
        self.assertNotEqual(my_model.created_at, my_model.updated_at)

    # ---------Test Save Method ---------------------------------------------

    def test_saveCorrect(self):
        """Tests that save works correctly"""
        my_model = BaseModel()
        sleep(1)
        my_model.save()
        self.assertEqual(my_model.created_at.second, my_model.updated_at.second - 1)


    # ---------Test __str__ Method ---------------------------------------------

    def test_strCorrect(self):
        """Test that str works correctly"""
        my_model = BaseModel()
        f = io.StringIO()
        s = "[BaseModel] ({}) {}\n".format(my_model.id, my_model.__dict__)
        with redirect_stdout(f):
            print(my_model)
        self.assertEqual(f.getvalue(), s)




    # ---------Test Save Method ---------------------------------------------
