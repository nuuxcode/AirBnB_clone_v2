#!/usr/bin/python3
""" doc doc """
import unittest
import os
@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db','Test is not relevant for db storage')
class test_DBStorage(unittest.TestCase):
    """ doc doc """

    def test(self):
        """ doc doc """
        pass
