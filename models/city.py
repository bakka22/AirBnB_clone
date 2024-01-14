#!/usr/bin/python3
""" user module """

from models.base_model import BaseModel
import models


class City(BaseModel):
    """ User class """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ special __init__ method """
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__()
