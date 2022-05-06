import os
class Config:
    '''
    General configuration parent class
    '''
    MOVIE_API_KEY='09e41b835383809c9a7358f1e7dd753b'
    MOVIE_API_BASE_URL ='https://api.themoviedb.org/3/movie/{}?api_key={}'
    SECRET_KEY=os.urandom(32)

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:ogaye@localhost/watchlist'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    #email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")





class ProdConfig(Config):
    '''
    Pruduction  configuration child class

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