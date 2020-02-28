#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import models
import os


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        # Use cascade="all, delete" here or on FK constraint in cities??
        # Does it matter where you use single or double quotes?
        # cities = relationship("City", cascade="all, delete", backref="state")
        cities = relationship("City", backref="state")
    else:
        @property
        def cities(self):
            """getter:
            self is a state object
            we use the state obj to
            to find city objects that
            have the same state id
            """
            city = models.storage.all()
            # print("in state.py!!!", city)
            listy = []
            for k, v in city.items():
                val = v.to_dict()
                if 'state_id' in val and val['state_id']:
                    if val['state_id'] == self.id:
                        listy.append(v)
                    # print("state.py --> id == {} \nstate.py ---> obj == {}".format(k, v['state_id']))

                # if self.id == obj.state_id:
                #     listy.append(obj)
            return listy
