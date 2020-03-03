import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'MtVnZrS20!8'
    SQLALCHEMY_DATABASE_URI = os.environ['postgres://ksmpozaoeoigiz:331f7566a499d1915891ee4fccabb249230d8105b7e4d8b4c957a8197f2907ca@ec2-52-203-160-194.compute-1.amazonaws.com:5432/d8htdmphqchies']


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
