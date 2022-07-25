import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Text, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Users(Base):
    __tablename__='Users'
    id = Column(Integer, primary_key=True)
    email = Column(String(80), nullable=False)
    password = Column(String(80), nullable=False)
    name = Column(String(80))
    lastname = Column(String(80))

class Character(Base):
    __tablename__='Characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(80))
    height = Column(Integer)		
    mass = Column(Integer)		
    hair_color = Column(String(80))	
    skin_color = Column(String(80))		
    eye_color = Column(String(80))		
    birth_year = Column(String(80))		
    gender = Column(String(80))

class Planet(Base):
    __tablename__='Planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(80))		
    rotation_period = Column(Integer)		
    orbital_period = Column(Integer)	
    diameter = Column(Integer)		
    climate = Column(String(80))		
    gravity = Column(String(80))
    terrain = Column(String(80))
    surface_water = Column(Integer)		
    population = Column(String(80))		
    residents_id = Column(Integer, ForeignKey(""))
    films_id = Column(Integer, ForeignKey(""))

class Film(Base):
    __tablename__='Films'
    id = Column(Integer, primary_key=True)
    title = Column(String(80))		
    episode_id = Column(Integer)		
    opening_crawl = Column(Text(500))		
    director = Column(String(80))		
    producer = Column(String(80))		
    release_date = Column(Date)		
    characters_id = Column(Integer, ForeignKey(""))
    planets_id = Column(Integer, ForeignKey(""))
    starships_id = Column(Integer, ForeignKey(""))
    vehicles_id = Column(Integer, ForeignKey(""))
    species_id = Column(Integer, ForeignKey(""))

class Specie(Base):
    __tablename__='Species'
    id = Column(Integer, primary_key=True)
    name = Column(String(80))		
    classification = Column(String(80))		
    average_height = Column(Integer)		
    skin_colors = Column(String(80))		
    hair_colors = Column(String(80))		
    eye_colors = Column(String(80))		
    average_lifespan = Column(Integer)		
    homeworld_id = Column(Integer, ForeignKey(""))
    language = Column(String(80))		
    people_id = Column(Integer, ForeignKey(""))
    films_id = Column(Integer, ForeignKey(""))

class Vehicle(Base):
    __tablename__='Vehicles'
    id = Column(Integer, primary_key=True)
    name = Column(String(80))		
    model = Column(String(80))		
    manufacturer = Column(String(80))		
    cost_in_credits = Column(Integer)	
    lenght = Column(Float)		
    max_atmosphering_speed = Column(Integer)	
    crew = Column(Integer)		
    passengers = Column(Integer)
    cargo_capacity = Column(Integer)
    consumables = Column(String(80))		
    vehicle_class = Column(String(80))		
    pilots_id = Column(Integer, ForeignKey(""))
    films_id = Column(Integer, ForeignKey(""))

class Starship(Base):
    __tablename__='Starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(80))		
    model = Column(String(80))		
    manufacturer = Column(String(80))		
    cos_in_credits = Column(Integer)		
    lenght = Column(Integer)		
    max_atmosphering_speed = Column(Integer)		
    crew = Column(String(80))		
    passengers = Column(Integer)		
    cargo_capacity = Column(Integer)		
    consumables = Column(String(80))		
    hyperdrive_rating = Column(String(80))		
    MGLT = Column(Integer)		
    starship_class = Column(String(80))		
    pilots_id = Column(Integer, ForeignKey(""))
    films_id = Column(Integer, ForeignKey(""))

class Favorite_Character(Base):
    __tablename__= 'Favorites Characters'
    users_id = Column(Integer, ForeignKey("Users.id"), primary_key=True)
    people_id = Column(Integer, ForeignKey("Characters.id"), primary_key=True)

class Favorite_Vehicle(Base):
    __tablename__= 'Favorites Vehicles'
    users_id = Column(Integer, ForeignKey("Users.id"))
    vehicle_id = Column(Integer, ForeignKey("Vehicles.id"), primary_key=True)

class Favorite_Planet(Base):
    __tablename__= 'Favorites Planets'
    users_id = Column(Integer, ForeignKey("Users.id"), primary_key=True)
    planets_id = Column(Integer, ForeignKey("Planets.id"), primary_key=True)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')