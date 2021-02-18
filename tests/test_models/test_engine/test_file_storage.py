#!/usr/bin/python3
"""
Unit tests for file_storage.py
"""

import unittest
import uuid
import json
import pep8
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel
from datetime import datetime as time

class TestCodeFormat(unittest.TestCase):

    def test_conformance(self):
        """Test that models/engine/file_storage.py conforms to PEP-8."""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


    def test_conformance(self):
        """Test that tests/test_models/test_engine/test_file_storage.py conforms to PEP-8."""
        style = pep8.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_engine/test_file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

class TestFileStorage(unittest.TestCase):
    """Tests to check file_storage"""

    def test_init1(self):
        '''test_init1 - testing basemodel'''
        base = BaseModel()
        self.assertIsInstance(base, BaseModel)
        self.assertIsInstance(base.created_at, time)
        self.assertIsInstance(base.updated_at, time)
        self.assertNotIsInstance(base.id, uuid.UUID)
        self.assertIsInstance(base.id, str)

    def test_str(self):
        '''test_str - testing string rep'''
        base2 = BaseModel()
        string = "[{}] ({}) {}".format(type(base2).__name__,
                                       base2.id, base2.__dict__)
        self.assertEqual(str(base2), string)

    def test_save(self):
        '''test_save - testing save in BaseModel'''
        base3 = BaseModel()
        old_base = base2.updated_at
        base2.save()
        self.assertNotEqual(old_base, base.updated_at)
