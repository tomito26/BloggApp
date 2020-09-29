import os
class Config:
    '''
    General configuration parent class
    '''
    QUOTES_API_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:tom@localhost/blogsite'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    #simple mde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

  


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