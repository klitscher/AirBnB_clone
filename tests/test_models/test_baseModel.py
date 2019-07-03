"""Test module for BaseModel class"""


import unittest
import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import os.path
import uuid


class TestBase(unittest.TestCase):
    """Tests for the BaseModel class"""

    def __init__(self, *args, **kwargs):
        """Method to set up data model to test"""

        super().__init__(*args, **kwargs)
        self._class = BaseModel
        self._name = "BaseModel"

    def test_id(self):
        """Test base model UUID is created properly"""

        base = self._class()
        with self.subTest(msg="id is a UUID"):
            self.assertIsInstance(base.id, str)
            self.assertIsInstance(uuid.UUID(base.id), uuid.UUID)
        with self.subTest(msg="IDs are unique"):
            self.assertNotEqual(self._class().id, self._class().id)

    def test_timeUpdate(self):
        """Test that the time is set and updated correctly"""

        base = self._class()
        with self.subTest(msg="Creation time"):
            now = datetime.datetime.now()
            self.assertIsInstance(base.updated_at, datetime.datetime)
            self.assertTrue(0 < (now - base.updated_at).total_seconds() < 1)
        with self.subTest(msg="Updated time"):
            old = base.updated_at
            base.save()
            now = datetime.datetime.now()
            self.assertTrue(old < base.updated_at < now)

    def test_str(self):
        """Test __str__ method in BaseModel class"""

        base = self._class()
        yes = "[" + self._name + "] ({}) {}".format(
            base.id, str(base.__dict__))
        self.assertEqual(str(base), yes)

    def test_createTime(self):
        """Tests creation time stamp for BaseModel"""

        base = self._class()
        now = datetime.datetime.now()
        self.assertIsInstance(base.created_at, datetime.datetime)
        self.assertTrue(0 < (now - base.created_at).total_seconds() < 1)

    def test_toDict(self):
        """Test converting to dictionary with to_dict"""

        base = self._class()
        dic = base.to_dict()
        with self.subTest(msg="Has all attributes"):
            a = set(dic.keys())
            b = set(base.__dict__.keys())
            self.assertTrue(b.issubset(a))
        with self.subTest(msg="class name added"):
            self.assertTrue("__class__" in dic.keys())
            self.assertEqual(dict["__class__"], self._name)
        with self.subTest(msg="times converted to string"):
            self.assertIsInstance(dic["created_at"], str)
            self.assertIsInstance(dic["updated_at"], str)
            self.assertEqual(dic["created_at"], base.created_at.isoformat())
            self.assertEqual(dic["updated_at"], base.updated_at.isoformat())
