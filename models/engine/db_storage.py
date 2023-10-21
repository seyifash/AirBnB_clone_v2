#!/usr/bin/python3
"""DB STORAGE"""


from os import getenv
from models.base_model import Base
from models.city import City
from models.state import State
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import (create_engine)
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm.session import sessionmaker


class DBStorage:
    """Represents DB STORAGE."""
    __engine = None
    __session = None

    def __init__(self):
        """initialization."""
        user = getenv('HBNB_MYSQL_USER')
        pwd = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        env = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
                                            user, pwd, host, db
                                        ))
        if env == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """get all of them."""
        dic = {}
        if cls:
            if type(cls) == str:
                cls = eval(cls)
            q = self.__session.query(cls)
            for el in q:
                key = "{}.{}".format(el.__class__.__name__, el.id)
                dic[key] = el
        else:
            classlist = [User, State, City, Amenity, Place, Review]
            for c in classlist:
                q = self.__session.query(c)
                for el in q:
                    key = "{}.{}".format(el.__class__.__name__, el.id)
                    dic[key] = el
        return dic

    def new(self, obj):
        """new ones are added here."""
        self.__session.add(obj)

    def save(self):
        """save them ( I mean the model instances)."""
        self.__session.commit()

    def delete(self, obj=None):
        """delete them!!!."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """get them back on track, like reload them, BRO!!!"""
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
