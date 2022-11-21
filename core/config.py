import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

database_uri = 'postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}'.format(
    db_user=os.getenv('DB_USER'),
    db_pass=os.getenv('DB_PASS'),
    db_host=os.getenv('DB_HOST'),
    db_port=os.getenv('DB_PORT'),
    db_name=os.getenv('DB_NAME')
)


class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = database_uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = database_uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False


app_config = {
    'development': Development,
    'production': Production
}