#!/usr/bin/python3
""" consle module """

from models.base_model import BaseModel
from models.user import User
from models import storage
import cmd

class HBNBCommand(cmd.Cmd):
	""" hbnb command interpreter """
	models = ["BaseModel", "User"]
	objs = storage.all()
	prompt = "(hbnb)"
	def find_id(self, id):
		""" check availabilty of id """
		for key in self.objs.keys():
			if id == self.objs[key].id:
				return 1
		return 0
	def do_EOF(self, line):
		""" ctrl + D exits prompt """
		return True
	def emptyline(self):
		""" an emptyline doesn't do anything """
		pass
	def do_quit(self, line):
		"""Quit command to exit the program"""
		return True
	def do_create(self, line):
		""" creates a new instance of a class """
		model, id = self.par(line)
		if not self.err_handeld(model, 1):
			return
		model = model + "()"
		new = eval(model)
		new.save()
		print(new.id)
	def par(self, line):
		""" parses a line """
		if not line:
			return [None, None]
		line = line.split()
		if len(line) >= 2:
			return line[:2]
		if len(line) == 1:
			return [line[0], None]
	def up_par(self, line):
		""" parses line into four argumenst """
		tmp = self.par(line)
		line = line.split(maxsplit=3)
		if len(line) < 2:
			return tmp + [None, None]
		if len(line) >= 4:
			return tmp + line[2:4]
		if len(line) == 3:
			return tmp + [line[2], None]
	def err_handeld(self, model, id):
		""" handle errors """
		if not model:
			print("** class name missing **")
			return 0
		if model not in self.models:
			print("** class doesn't exist **")
			return 0
		if not id:
			print("** instance id missing **")
			return 0
		found = self.find_id(id)
		if id == 1:
			found = 1
		if not found:
			print("** no instance found **")
			return 0
		return 1
	def up_err(self, attr, val):
		""" handel update errors """
		if not attr:
			print("** attribute name missing **")
			return 0
		if not val:
			print("** value missing **")
			return 0
		return 1
	def do_show(self, line=None):
		""" prints the string representation of an instance """
		model, id = self.par(line)
		if not self.err_handeld(model, id):
			return
		print(self.objs[model + '.' + id])
	def do_destroy(self, line):
		""" destroy an instance based on id """
		model, id = self.par(line)
		if not self.err_handeld(model, id):
			return
		del self.objs[model + "." + id]
		storage.save()
	def do_all(self, line):
		""" prints all string representation of all instances """
		tmp = []
		model = self.par(line)[0]
		if model and model not in self.models:
			print("** class doesn't exist **")
			return
		if model:
			tmp = [str(f) for f in self.objs.values() if f.to_dict()['__class__'] == model]
		else:
			for model in self.models:
				tmp = tmp + [str(f) for f in self.objs.values() if f.to_dict()['__class__'] == model]
		print(tmp)
	def do_update(self, line):
		""" updates an instance based on class name an id """
		model, id, attr, val = self.up_par(line)
		if not self.err_handeld(model, id) or not self.up_err(attr, val):
			return
		tmp = self.objs[model + "." + id]
		if val[0] == '"':
			val = val.split('"')[1]
			tmp.__dict__[attr] = val
		else:
			tmp.__dict__[attr] = eval(val)
		tmp.save()

if __name__ == '__main__':
	HBNBCommand().cmdloop()
