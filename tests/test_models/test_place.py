#!/usr/bin/python3
""" test ModelBase """


import unittest
from models.base_model import BaseModel
from models.place import Place

class Place_Test(unittest.TestCase):
	""" test BaseModel """

	def test_inherit(self):
		""" test inherit from base """
		self.assertEqual(Place.__bases__, (BaseModel, ))

	def test_has_attr(self):
		""" test presence of attr """
		re = Place()
		self.assertTrue(hasattr(re, "id"), True)

if __name__ == "__main__":
	unittest.main()
