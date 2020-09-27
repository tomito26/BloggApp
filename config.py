import os
class Config:
    '''
    General configuration parent class
    '''
    QUOTES_API_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:tom@localhost/blogapp'


class ProdConfig(Config):
    '''
    Production configuration child class
    
    Args:
        Config:The parent configuration class with General configuration settings
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration class with general configuration settings
    '''
    DEBUG = True


config_options = {
    'development':DevConfig,
    'production':ProdConfig
}