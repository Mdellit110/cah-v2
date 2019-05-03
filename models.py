from sqlalchemy import Column, Integer, String, create_engine

from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql+psycopg2://matthewdellitalia:fla1996md@localhost/cah', echo=True)
connection = engine.connect()

Base = declarative_base()

class UserModel(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    last_name = Column(String)

class WhiteCardModel(Base):
    __tablename__ = 'white_cards'
    id = Column(Integer, primary_key=True)
    deck = Column(String)
    icon = Column(String)
    text = Column(String)

class BlackCardModel(Base):
    __tablename__ = 'black_cards'
    id = Column(Integer, primary_key=True)
    pick = Column(Integer)
    deck = Column(String)
    text = Column(String)
    icon = Column(String)
