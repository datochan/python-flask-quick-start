import os
import logging
from flask import Blueprint, jsonify, current_app
from werkzeug.exceptions import HTTPException
from flask_quick.exceptions import APIException

quick_flask = Blueprint('flask_quick', __name__)


@quick_flask.app_errorhandler(Exception)
def framework_error(e):
    """
    处理未知错误
    """
    if isinstance(e, APIException):
        # 已知异常直接返回
        return e

    if isinstance(e, HTTPException):
        code = e.code
        message = e.description
        return str(APIException(message, code))

    else:
        if current_app.config['FLASK_CONFIG'] != "development":
            return str(APIException())
        else:
            raise e


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
                                                                    "?charset=utf8"

    @staticmethod
    def init_app(app):
        pass


from . import lib, views
