#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from os import getenv
from models.review import Review
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer, ForeignKey, Float, Table
from sqlalchemy.orm import relationship

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60), ForeignKey('places.id'),
                             primary_key=True, nullable=False)
                     # Column('amenity_id', String(60),
                      #       ForeignKey('amenities.id'),
                       #      primary_key=True, nullable=False))
                       )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship('Review', backref='place')
        #amenities = relationship(
        #    "Amenity",
         #   secondary=place_amenity,
          #  viewonly=False,
           # backref="place_amenities")
    else:
        @property
        def reviews(self):
            """getter function for reviews."""
            review_list = []
            reviews_dic = models.storage.all(Review)
            for obj in reviews_dic.values():
                if obj.place_id == self.id:
                    review_list.append(obj)
            return review_list

        @property
        def amenities(self):
            """getter function for amenities."""
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj):
            """setter function for amenities method."""
            if obj.__class__.__name__ == 'Amenity':
                if obj.id not in self.amenity_ids:
                    self.amenity_ids.append(obj.id)
