#!/usr/bin/python3
""" user module """

from models.base_model import BaseModel
from models import storage

class User(BaseModel):
	""" User class """
	email = ""
	password = ""
	first_name = ""
	last_name = ""
	def __init__(self, *args, **kwargs):
		""" special __init__ method """
		if kwargs:
			super.__init__(**kwargs)
		else:
			super.__init__()

