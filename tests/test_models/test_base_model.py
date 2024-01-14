#!/usr/bin/python3
""" test ModelBase """


import unittest
from models.base_model import BaseModel


class BaseModel_Test(unittest.TestCase):
    """ test BaseModel """

    def test_inherit(self):
        """ test inherit from base """
        self.assertEqual(BaseModel.__bases__, (object, ))

    def test_has_attr(self):
        """ test presence of attr """
        re = BaseModel()
        self.assertTrue(hasattr(re, "id"), True)


if __name__ == "__main__":
    unittest.main()
