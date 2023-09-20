#!/usr/bin/python3
""" document documt """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ document documt """

    def __init__(self, *args, **kwargs):
        """ document documt """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ document documt """
        new = self.value()
        self.assertEqual(type(new.name), str)
