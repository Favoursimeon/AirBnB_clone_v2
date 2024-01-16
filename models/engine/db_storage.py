#!/usr/bin/python3
"""Defines a data stroage class"""

from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """DB class"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiation method"""
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)
        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database session"""
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)

            query = self.__session.query(cls)
            for row in query:
                key = "{}.{}".format(cls.__name__, row.id)
                dic[key] = row
        else:
            classes = [User, State, City, Amenity, Place, Review]
            for i in classes:
                query = self.__session.query(i)
                for row in query:
                    key = "{}.{}".format(i.__name__, row.id)
                    dic[key] = row

        return dic

    def new(self, obj):
        """adds new element to db session"""
        self.__session.add(obj)

    def save(self):
        """saves the session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete an element in the table
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """configures the db session"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Session)
        self.__session = Session()
