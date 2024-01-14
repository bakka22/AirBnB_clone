#!/usr/bin/python3
""" test ModelBase """


import unittest
from models.base_model import BaseModel
from models.state import State


class State_Test(unittest.TestCase):
    """ test BaseModel """

    def test_inherit(self):
        """ test inherit from base """
        self.assertEqual(State.__bases__, (BaseModel, ))

    def test_has_attr(self):
        """ test presence of attr """
        re = State()
        self.assertTrue(hasattr(re, "id"), True)


if __name__ == "__main__":
    unittest.main()
