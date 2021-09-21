# server/config.py


import os
basedir = os.path.abspath(os.path.dirname(__file__))
postgres_local_base = 'postgresql://postgres:953515@localhost:5433/'
database_name = 'da-flask-app'


class BaseConfig:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', '\xc5^\xd3\xd6\xa3\x92c4\xc1\x00O87\xd5\xd0\x8f\xc7\x89\xdc\x10\xd4\xf2\x94\xb5')
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name + '_test'
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(BaseConfig):
    """Production configuration."""
    SECRET_KEY = '\xc5^\xd3\xd6\xa3\x92c4\xc1\x00O87\xd5\xd0\x8f\xc7\x89\xdc\x10\xd4\xf2\x94\xb5'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgres://qhtjvehionrpvj:62d2995d3b607c0260d84eb37736dbec8d5b3e8ab4a3c4bcd358ee4b92288336@ec2-52-208-221-89.eu-west-1.compute.amazonaws.com:5432/d4qs27m374c0qh'
