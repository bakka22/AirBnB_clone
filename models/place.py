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
	number_rooms = 0
	number_bathrooms = 0
	max_guest = 0
	price_by_night = 0
	latitude = 0.0
	longitude = 0.0
	amenity_ids = []
	def __init__(self, *args, **kwargs):
		""" special __init__ method """
		if kwargs:
			super().__init__(**kwargs)
		else:
			super().__init__()

