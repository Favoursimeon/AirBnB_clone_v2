#!/usr/bin/python3
""" State Module for HBNB project """
import shlex

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
import shlex
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        all = models.storage.all()
        city_list = []
        res = []
        for key in all.keys():
            attr = key.replace(',', ' ')
            attr = shlex.split(attr)
            if attr[0] == 'City':
                city_list.append(all[key])
        for obj in city_list:
            if obj.state_id == self.id:
                res.append(obj)
        return res
