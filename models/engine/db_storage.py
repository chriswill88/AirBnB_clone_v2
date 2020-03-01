#!/usr/bin/python3
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session

# imports from model Classes
from models.base_model import BaseModel, Base
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.city import City
import os


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                getenv('HBNB_MYSQL_USER'),
                getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST'),
                getenv('HBNB_MYSQL_DB')),
                pool_pre_ping=True)
        # Base.metadata.create_all(self.__engine)
        self.reload()
        if 'test' in os.environ and os.environ['HBNB_ENV'] == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):  # JFK added =none
        dic = {}
        a = 0
        query_list = [User, State, City, Amenity, Place, Review]
        if cls is None:
            # print("db storage - no class")
            for i in query_list:
                for x in self.__session.query(i):
                    # print(a, "----->>", x)
                    a += 1
                    dic["{}.{}".format(type(x).__name__, x.id)] = x

        else:
            # print("db storage - class", type(cls), query_list)
            for i in query_list:
                # print("i -->", i.__name__, cls)
                if i.__name__ == cls:
                    # print("found")
                    cls = i
                    break
            for lol in self.__session.query(cls):
                # print("A is ", lol)
                key = "{}.{}".format(type(lol).__name__, lol.id)
                dic[key] = lol
        return dic

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        sessionista = sessionmaker(
            bind=self.__engine,
            expire_on_commit=False)
        Session = scoped_session(sessionista)
        self.__session = Session()

    def close(self):
        self.__session.close()
