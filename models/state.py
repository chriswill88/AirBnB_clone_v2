#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    # Use cascade="all, delete" here or on FK constraint in cities??
    # Does it matter where you use single or double quotes?
    # cities = relationship("City", cascade="all, delete", backref="state")
    cities = relationship("City", backref="state")
    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """getter:
            self is a state object
            we use the state obj to
            to find city objects that
            have the same state id
            """
            cities = models.storage.all('City')
            listy = []
            for obj in cities.values():
                print("state.py --> id == {}, obj == {}".format(self.id, obj))
                if self.id == obj.state_id:
                    listy.append(obj)
            return listy
