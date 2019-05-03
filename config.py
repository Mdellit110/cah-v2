import os

class Config(object):
    PG_USERNAME = os.environ.get('PG_USERNAME') or 'PostgreSQL'
    PG_PASSWORD = os.environ.get('PG_PASSWORD') or 'PostgreSQL'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'like-really-secret-dude'
