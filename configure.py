# -*- coding: utf-8 -*-

import os
import sys
import logging

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(PROJECT_ROOT, 'dtrader'))


class Config:
    def __init__(self):
        pass

    SECRET_KEY = os.environ.get('SECRET_KEY') or ''

    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    LOGGER_LEVEL = logging.DEBUG
    LOGGER_FORMAT = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
    LOGGER_DATE_FORMAT = '%a, %d %b %Y %H:%M:%S'
    LOGGER_FILENAME = 'python-flask.log'
    LOGGER_FILEMODE = 'w'

    CACHE_TYPE = 'simple'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or "mysql+pymysql://root@localhost:3306/flask-dev" \
                                                                    "?charset=utf8 "


class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'mysql+pymysql://root@localhost:3306/flask?charset=utf8'

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
