import os
from secrets import *

class Config(object):
    PG_USERNAME = os.environ.get('PG_USERNAME') or PG_USERNAME_SECRET
    PG_PASSWORD = os.environ.get('PG_PASSWORD') or PG_PASSWORD_SECRET
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'like-really-secret-dude'
