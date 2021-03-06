from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import (scoped_session, sessionmaker)
from sqlalchemy.ext.declarative import declarative_base

from config import Config

engine = create_engine(f'postgresql+psycopg2://{Config.PG_USERNAME}:{Config.PG_PASSWORD}@localhost/cah', convert_unicode=True, echo=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

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

WhiteCardModel.__table__.create(bind=engine, checkfirst=True)
BlackCardModel.__table__.create(bind=engine, checkfirst=True)
