#!/usr/bin/python3
""" test ModelBase """


import unittest
from models.base_model import BaseModel
from models.city import City


class City_Test(unittest.TestCase):
    """ test BaseModel """

    def test_inherit(self):
        """ test inherit from base """
        self.assertEqual(City.__bases__, (BaseModel, ))

    def test_has_attr(self):
        """ test presence of attr """
        re = City()
        self.assertTrue(hasattr(re, "id"), True)


if __name__ == "__main__":
    unittest.main()
