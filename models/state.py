#!/usr/bin/python3
""" States Module for HBNB project"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
import models
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if (os.getenv("HBNB_TYPE_STORAGE") != "db"):
        @property
        def cities(self):
            """Get a list of all related City objects."""
            city = []
            for obj in list(models.storage.all(City).values()):
                if obj.state_id == self.id:
                    city.append(obj)
            return city
