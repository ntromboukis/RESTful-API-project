from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(Integer, primary_key = True)
    restaurant_name = Column(String(80), nullable = False)
    restaurant_address = Column(String)
    restaurant_image = Column(String)
    #Add add a decorator property to serialize data from the database
    @property
    def serialize(self):
        return {
        'restaurant_name'     : self.restaurant_name,
        'id'                  : self.id,
        'restaurant_address' : self.restaurant_address,
        'restaurant_image'    : self.restaurant_image
        }


engine = create_engine('sqlite:///restaurants.db')
Base.metadata.create_all(engine)
