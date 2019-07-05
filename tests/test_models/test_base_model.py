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

    def setUp(self):
        """Set up which instance to call"""
        self._class = BaseModel()
        self._class2 = BaseModel()
        self._name = "BaseModel"

    # -------------Tests Public Attributes-------------------------------

    def test_idCorrect(self):
        """Test that id is a unique string"""
        my_model1 = self._class
        my_model2 = self._class2
        self.assertTrue((type(my_model1.id) is str))
        self.assertNotEqual(my_model1.id, my_model2.id)

    def test_createUpdateType(self):
        """Test that create and update are datetime objects"""
        my_model = self._class
        self.assertTrue(isinstance(my_model.created_at, datetime))
        self.assertTrue(isinstance(my_model.updated_at, datetime))

    def test_updateDif(self):
        """Test that update is different than create after update"""
        my_model = self._class
        self.assertEqual(my_model.created_at.second,
                         my_model.updated_at.second)
        s1 = my_model.created_at.second
        sleep(1)
        my_model.name = "Holberton"
        s2 = my_model.updated_at.second
        self.assertEqual(s1, s2)

    # ---------Test Save Method --------------------------------

    def test_saveCorrect(self):
        """Tests that save works correctly"""
        my_model = self._class
        s1 = my_model.created_at.second
        sleep(1)
        my_model.save()
        s2 = my_model.updated_at.second
        if (s2 == 0):
            s2 = 60
        self.assertEqual(s1, s2 - 1)

    def test_saveArgs(self):
        """Tests passing args to save"""
        my_model = self._class
        self.assertRaises(TypeError, my_model.save, "Test")

    # ---------Test to_dict Method ----------------------------

    def test_toDictCorrect(self):
        """Tests that it works"""
        my_model = self._class
        dic = my_model.to_dict()
        flag = True
        for key, value in my_model.__dict__.items():
            if key not in dic:
                flag = False
        self.assertTrue(flag)

    def test_toDictClass(self):
        """Tests that __class__ was added"""
        my_model = self._class
        dic = my_model.to_dict()
        flag = True
        for key, value in dic.items():
            if "__class__" not in dic:
                flag = False
        self.assertTrue(flag)

    def test_toDictCreatedFormat(self):
        """Tests that created_at is in correct format"""
        my_model = self._class
        correct = datetime.isoformat(my_model.created_at)
        dic = my_model.to_dict()
        flag = True
        if correct not in dic.values():
                flag = False
        self.assertTrue(flag)

    def test_toDictUpdatedFormat(self):
        """Tests that updated_at is in correct format"""
        my_model = self._class
        correct = datetime.isoformat(my_model.updated_at)
        dic = my_model.to_dict()
        flag = True
        if correct not in dic.values():
                flag = False
        self.assertTrue(flag)

    def test_toDictArgs(self):
        """Tests passing args to to_dict"""
        my_model = self._class
        self.assertRaises(TypeError, my_model.to_dict, "Test")

    # ---------Test __str__ Method ---------------------------------

    def test_strCorrect(self):
        """Test that str works correctly"""
        my_model = self._class
        f = io.StringIO()
        s = "[{}] ({}) {}\n".format(self._name, my_model.id, my_model.__dict__)
        with redirect_stdout(f):
            print(my_model)
        self.assertEqual(f.getvalue(), s)
