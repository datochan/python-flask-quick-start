from .api import APIException


class ParameterException(APIException):
    code = 400
    message = '提交参数有误 ...'
 

class AuthFailed(APIException):
    code = 401
    message = '请先登录 ...'
 

class Forbidden(APIException):
    code = 403
    message = '权限不足 ...'
 

class NotFound(APIException):
    code = 404
    message = '服务未发现...'


class MethodNotAllowed(APIException):
    code = 405
    message = '请求方式不合法 ...'
 

class ServerError(APIException):
    code = 500
    message = '服务器发生内部错误 ...'


class ServiceMaintain(APIException):
    code = 503
    message = '服务维护中 ...'


class AccountRepeatException(APIException):
    code = 400
    message = APIException.message
