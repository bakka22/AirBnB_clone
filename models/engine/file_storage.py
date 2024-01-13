#!/usr/bin/python3
""" file storage module """


import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
class FileStorage():
	""" file storage class """
	__file_path = "storage.json"
	__objects = {}
	def all(self):
		""" returns the dictionary __opjects """
		return self.__objects
	def new(self, obj):
		""" sets in __opjects the opj with key <opj class name>.id """
		self.__objects[type(obj).__name__ + "." + obj.id] = obj
	def save(self):
		""" serialize __opjects to json file """
		tmp = self.__objects
		tmp2 = {k :tmp[k].to_dict() for k in tmp.keys()}
		with open(self.__file_path, "w") as f:
			json.dump(tmp2, f)
	def reload(self):
		""" deserializes the json file to __opjects """
		try:
			with open(self.__file_path, "r") as f:
				tmp = json.load(f)
				for i in tmp.values():
					name = i["__class__"]
					self.new(eval(name)(**i))
		except (FileNotFoundError, json.decoder.JSONDecodeError):
			pass
