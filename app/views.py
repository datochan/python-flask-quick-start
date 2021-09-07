# -*- coding: utf-8 -*-
"""
    core.views
    ~~~~~~~~~~~~~~
    项目的演示代码.
    :copyright: (c) 2019-10-08 by datochan.
"""
from app import __app__


@__app__.route('/', methods=['GET', 'POST'])
def index():
    return 'Hello, It Works!'
