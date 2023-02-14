from flask import json
from werkzeug.exceptions import HTTPException


class APIException(HTTPException):
    code = 500
    message = 'Internal Server Error'

    def __str__(self):
        resp = json.dumps({
            "code": self.code,
            "message": self.message,
            "data": "{}",
        })
        return resp

    def __init__(self, msg=None, code=None, scode=None):
        if code:
            self.code = code
        if msg:
            self.message = msg
            
        super(APIException, self).__init__(msg, None)

    def get_body(self, environ=None):
        body = dict(message=self.message, data={})
        text = json.dumps(body)
        return text

    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]
