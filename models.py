from sqlalchemy import Column, Integer, String

from sqlalchemy.ext.declarative import declarative_base

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
