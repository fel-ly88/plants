from sqlalchemy import Column, Integer, String, ForeignKey, Date, Float
from sqlalchemy.orm import relationship
from .database import Base

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String)
    plants = relationship('Plant', back_populates='category')

class Plant(Base):
    __tablename__ = 'plants'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    species = Column(String)
    location = Column(String)
    watering_frequency = Column(Integer)
    category_id = Column(Integer, ForeignKey('categories.id'))
    category = relationship('Category', back_populates='plants')
    waterings = relationship('Watering', back_populates='plant')

class Watering(Base):
    __tablename__ = 'waterings'
    id = Column(Integer, primary_key=True)
    plant_id = Column(Integer, ForeignKey('plants.id'))
    date = Column(Date)
    amount = Column(Float)
    plant = relationship('Plant', back_populates='waterings')
