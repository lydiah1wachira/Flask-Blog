import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = 'h4TvVu03'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wachira:Lydiah007@localhost/blogs'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
    @staticmethod
    def init_app(app):
        pass
  



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
    }