#!/usr/bin/python3
'''Unit testing for Place'''
import unittest
import uuid
import json
from models.base_model import BaseModel
from models.place import Place
from datetime import datetime as time


class TestPlace(unittest.TestCase):
    '''TestPlace - unit testing class'''

    def test_init1(self):
        '''test_init1 - testing Place'''
        place = Place()
        self.assertIsInstance(place, BaseModel)
        self.assertIsInstance(place.created_at, time)
        self.assertIsInstance(place.updated_at, time)
        self.assertNotIsInstance(place.id, uuid.UUID)
        self.assertIsInstance(place.id, str)
