#!/usr/bin/python3
""" """
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.state import State
from models.base_model import BaseModel


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_attributes_presence(self):
        """attributes presence."""
        new = self.value()
        self.assertTrue('name' in new.__dict__)
        self.assertTrue('cities' in new.__dict__)

    @unittest.skipIf(getenv('HBNB_TYPE_STORAGE') == 'db', 'Not db storage')
    def test_cities_returnvalue(self):
        """cities return value."""
        instance = self.value()
        self.assertEqual(type(instance.cities()), list)

    def test_subclass(self):
        """testing for subclass."""
        instance = self.value()
        self.assertTrue(issubclass(instance.__class__, BaseModel), True)
