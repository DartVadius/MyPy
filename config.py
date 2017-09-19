import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    CSRF_ENABLED = True
    SECRET_KEY = 'very-very-secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
