#!/usr/bin/python3
""" file storage module """


import json


class FileStorage():
	""" file storage class """
	__file_path = "storage.json"
	__opjects = {}
	def all(self):
		""" returns the dictionary __opjects """
		return self.__opjects
	def new(self, obj):
		""" sets in __opjects the opj with key <opj class name>.id """
		self.__opjects[type(obj).__name__ + "." + obj.id] = obj.to_dict()
	def save(self):
		""" serialize __opjects to json file """
		with open(self.__file_path, "w") as f:
			json.dump(self.__opjects, f)
	def reload(self):
		""" deserializes the json file to __opjects """
		try:
			with open(self.__file_path, "r") as f:
				self.__opjects = json.load(f)
		except (FileNotFoundError, json.decoder.JSONDecodeError):
			pass
