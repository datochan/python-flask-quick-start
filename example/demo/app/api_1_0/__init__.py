from flask import Blueprint, jsonify, current_app
from flask.json import loads
from werkzeug.exceptions import HTTPException
from flask_quick.exceptions import APIException

__api_1_0 = Blueprint('api', __name__)

from . import views


@__api_1_0.after_request
def after_request(response):
    """
    请求处理后,用来对返回的response进行加密
    :return:
    GET: 200 OK
    POST: 201 Created
    PUT: 200 OK
    PATCH: 200 OK
    DELETE: 204 No Content
    """
    if response.status_code == 200 or response.status_code == 201 or \
        response.status_code == 202 or response.status_code == 204:
        resp = loads(response.response[0])

        response = jsonify({
            "code": 0,
            "message": resp.get("message", "success"),
            "data": resp.get("data", {})
        })

    return response


@__api_1_0.app_errorhandler(Exception)
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
        return APIException(message, code)

    else:
        if current_app.config['FLASK_CONFIG'] != "development":
            return APIException()
        else:
            raise e
