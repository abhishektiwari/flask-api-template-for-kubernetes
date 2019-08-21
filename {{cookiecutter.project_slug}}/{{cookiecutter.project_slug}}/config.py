"""
Configuration options for app
"""
import os
from datetime import timedelta

# Secret keys are generated using
# Alt-1:
# import os
# import binascii
# binascii.hexlify(os.urandom(48))
# Alt-2:
# ssh-keygen -t rsa -b 2048 -f jwtRS256_NAME.key
# Secret keys are stored in secret store

POSTGRES = {
    'user': os.environ.get('POSTGRES_USER'),
    'password': os.environ.get('POSTGRES_PASSWORD'),
    'db_name': os.environ.get('POSTGRES_DB_NAME'),
    'host': os.environ.get('POSTGRES_HOST') or 'localhost', # localhost for dev
    'port': os.environ.get('POSTGRES_PORT') or 5432 # Standard port 5432
}

DB_URI = 'postgres://%(user)s:%(password)s@%(host)s:%(port)s/%(db_name)s' % POSTGRES

class Config:
    """Common config"""
    JWT_TOKEN_LOCATION = ['headers', 'cookies']
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=30)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=7)
    JWT_ALGORITHM = 'HS256'
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    POSTGRES_USER = os.environ.get('POSTGRES_USER')
    POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
    POSTGRES_HOST = os.environ.get('POSTGRES_HOST')
    SQLALCHEMY_DATABASE_URI = DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        """init app"""
        pass #pylint: disable-msg=W0107

class DevelopmentConfig(Config):
    """Dev specific config"""
    DEBUG = True

class ProductionConfig(Config):
    """Prod specific config"""
    DEBUG = False
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

#pylint: disable-msg=C0103
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
