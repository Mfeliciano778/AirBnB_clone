#!/usr/bin/python3
"""
Unit tests for file_storage.py
"""

import unittest
import uuid
import json
import pycodestyle
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
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


    def test_conformance(self):
        """Test that tests/test_models/test_engine/test_file_storage.py conforms to PEP-8."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_engine/test_file_storage.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

