#!/usr/bin/python3
'''Unit testing for User'''
import unittest
import uuid
import json
from models.base_model import BaseModel
from models.user import User
from datetime import datetime as time


class TestUser(unittest.TestCase):
    '''TestUser - unit testing class'''

    def test_init1(self):
        '''test_init1 - testing User'''
        user = User()
        self.assertIsInstance(user, BaseModel)
        self.assertIsInstance(user.created_at, time)
        self.assertIsInstance(user.updated_at, time)
        self.assertNotIsInstance(user.id, uuid.UUID)
        self.assertIsInstance(user.id, str)

    def test_empty(self):
        '''test_empty - testing for an empty attributes'''
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)
        self.assertIsInstance(user.password, str)
