from .api import APIException


class ParameterException(APIException):
    code = 400
    service_code = 4000
    message = '提交参数有误 ...'
 

class ClientTypeError(APIException):
    code = 400
    service_code = 4001
    message = '无效请求 ...'
 

class AuthFailed(APIException):
    code = 401
    service_code = 4010
    message = '请先登录 ...'
 

class Forbidden(APIException):
    code = 403
    service_code = 4030
    message = '权限不足 ...'
 

class NotFound(APIException):
    code = 404
    service_code = 4040
    message = '服务未发现...'


class MethodNotAllowed(APIException):
    code = 405
    service_code = 4050
    message = '请求方式不合法 ...'
 

class ServerError(APIException):
    code = 500
    service_code = 5000
    message = '服务器发生内部错误 ...'


class ServiceMaintain(APIException):
    code = 503
    service_code = 5030
    message = '服务维护中 ...'


class AccountRepeatException(APIException):
    code = 400
    service_code = 4000
    message = APIException.message