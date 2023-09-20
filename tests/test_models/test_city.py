#!/usr/bin/python3
""" document documt """
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """ document documt """

    def __init__(self, *args, **kwargs):
        """ document documt """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ document documt """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """ document documt """
        new = self.value()
        self.assertEqual(type(new.name), str)
