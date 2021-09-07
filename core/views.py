# -*- coding: utf-8 -*-
"""
    core.views
    ~~~~~~~~~~~~~~
    项目的演示代码.
    :copyright: (c) 2019-10-08 by datochan.
"""
from core import __core__


@__core__.route('/', methods=['GET', 'POST'])
def index():
    return 'Hello, It Works!'
