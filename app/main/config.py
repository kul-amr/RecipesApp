import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY','DEV_KEY')


class DevelopmentConfig(Config):

    # SQLALCHEMY_DATABASE_URI = postgres_local_base
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'recipesapp.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):

    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'recipesapp_test.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):

    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'recipesapp_prod.db')


config_names = dict(dev = DevelopmentConfig, test = TestingConfig, prod = ProductionConfig)
key = Config.SECRET_KEY