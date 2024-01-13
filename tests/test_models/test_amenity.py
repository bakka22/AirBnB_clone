#!/usr/bin/python3
""" test ModelBase """


import unittest
from models.amenity import Amenity
from models.base_model import BaseModel

class amenity_Test(unittest.TestCase):
	""" test BaseModel """

	def test_inherit(self):
		""" test inherit from base """
		self.assertEqual(amenity.__bases__, (BaseModel, ))

	def test_has_attr(self):
		""" test presence of attr """
		re = Amenity()
		self.assertTrue(hasattr(re, "id"), True)

if __name__ == "__main__":
	unittest.main()
