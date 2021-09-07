# -*- coding: utf-8 -*-
"""
    index
    ~~~~~~~~~~~~~~
    系统首页

    :copyright: (c) 19/10/08 by datochan.
"""
from flask import jsonify
from app.api_1_0 import __api_1_0


@__api_1_0.route('/', methods=['GET'])
def index():
    """
    首页
    :return:
    """
    resp = {"page": "index"}
    return jsonify(message="成功", data=resp)
