
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurant'


    name = Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    location = Column(String(250))
    photoUrl = Column(String(250))
    #Add add a decorator property to serialize data from the database
    @property
    def serialize(self):
        return {
        'name'          : self.name,
        'id'            : self.id,
        'location'      : self.location,
        'photo'         : self.photoUrl
        }


engine = create_engine('sqlite:///restaurant.db')
Base.metadata.create_all(engine)
