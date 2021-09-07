import os
import logging
from flask import Blueprint

quick_flask = Blueprint('quick_flask', __name__)

APP_MODULES = [
    {"entry": quick_flask},
]


class Configure(object):
    def __init__(self):
        pass

    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or ''

    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    LOGGER_LEVEL = logging.DEBUG
    LOGGER_FORMAT = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
    LOGGER_DATE_FORMAT = '%a, %d %b %Y %H:%M:%S'
    LOGGER_FILENAME = 'python-flask.log'
    LOGGER_FILEMODE = 'w'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or "mysql+pymysql://root@localhost:3306/flask-dev" \
                                                                    "?charset=utf8 "

    @staticmethod
    def init_app(app):
        pass


from . import lib, views
