#!/usr/bin/python3
""" user module """

from models.base_model import BaseModel
import models

class Place(BaseModel):
	""" User class """
	city_id = ""
	user_id = ""
	name = ""
	description = ""
	number_rooms = ""
	number_bathrooms = ""
	max_guest = ""
	price_by_night = ""
	latitude = 0.0
	longitude = 0.0
	amenity_ids = []
	def __init__(self, *args, **kwargs):
		""" special __init__ method """
		if kwargs:
			super().__init__(**kwargs)
		else:
			super().__init__()

