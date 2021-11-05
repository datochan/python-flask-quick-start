from flask import json
from werkzeug.exceptions import HTTPException


class APIException(HTTPException):
    code = 500
    service_code = None
    message = 'Internal Server Error'

    def __str__(self):
        resp = json.dumps({
            "code": self.code,
            "service_code": self.service_code,
            "message": self.message,
        })
        return resp

    def __init__(self, msg=None, code=None, scode=None):
        if code:
            self.code = code
        if scode:
            self.service_code = scode
        if msg:
            self.message = msg
            
        super(APIException, self).__init__(msg, None)

    def get_body(self, environ=None):
        body = dict(message=self.message, data={}, code= self.service_code)
        text = json.dumps(body)
        return text

    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]
