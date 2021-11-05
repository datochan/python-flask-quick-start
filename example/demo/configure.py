#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = 'gordon'

import os
import sys
import logging
from flask_quick import Configure

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
sys.path.append(os.path.join(PROJECT_ROOT, 'app'))


class DemoConfig(Configure):
    def __init__(self):
        pass

    JSON_AS_ASCII = False

    SECRET_KEY = os.environ.get('SECRET_KEY') or ''

    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    LOGGER_LEVEL = logging.DEBUG
    LOGGER_FORMAT = '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
    LOGGER_DATE_FORMAT = '%a, %d %b %Y %H:%M:%S'
    LOGGER_FILENAME = 'nike.log'
    LOGGER_FILEMODE = 'w'

    @staticmethod
    def init_app(app):
        pass


class DemoConfigDev(DemoConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'mysql+pymysql://root@localhost:3306/demo?charset=utf8'


class DemoConfigProd(DemoConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'mysql+pymysql://root@localhost:3306/demo?charset=utf8'

    @classmethod
    def init_app(cls, app):
        Configure.init_app(app)


config = {
    'development': DemoConfigDev,
    'production': DemoConfigProd,
    'default': DemoConfigDev
}
