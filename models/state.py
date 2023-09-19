#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import String, Column


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref="state")

    @property
    def cities(self):
        obj_list = []
        objs = models.storage.all(City)
        for obj in objs.values():
            if obj.state_id == self.id:
                obj_list.append(obj)
        return obj_list
