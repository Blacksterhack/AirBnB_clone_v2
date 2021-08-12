#!/usr/bin/python3
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
import os
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.review import Review
from models.user import User
from models.place import Place
from models.base_model import Base, BaseModel


class DBStorage():
    """
    New engine DBStorage
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        constructor
        """
        user = os.getenv("HBNB_MYSQL_USER")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        # will be localhost
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        connection = 'mysql+mysqldb://{}:{}@localhost/{}'
        self.__engine = create_engine(connection.format(
            user, pwd, db), pool_pre_ping=True)
        if (os.getenv("HBNB_ENV") == "test"):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        return the dictionary of cls
        """
        dicc = {}
        if cls:
            query = self.__session.query(eval(cls))
            for clase in query:
                key = "{}.{}".format(type(clase).__name__, clase.id)
                dicc[key] = clase
        else:
            lista_clases = [User, State, City, Amenity, Place, Review]
            for clase in lista_clases:
                query = self.__session.query(clase)
                for obj in query:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    dicc[key] = obj
        return dicc

    def new(self, obj):
        """
        add a new object to db
        """
        self.__session.add(obj)

    def save(self):
        """
        commit  the objetc to db
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session
        obj if not None
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database
        """
        # create tables into a db
        Base.metadata.create_all(self.__engine)
        # creamos el session object
        # expire_on_commmot = false >>> ignore the query sql
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()

    def close(self):
        """ Close method. """
        self.__session.close()
