from os import getcwd
from os.path import join


class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://mysql:mysql@localhost/mus_platform'
    SECRET_KEY = 'MY-secret-key-you-will-never-guess'
    UPLOAD_FOLDER = join(getcwd(), 'static/songs')
    FLASK_ADMIN_SWATCH = 'cerulean'