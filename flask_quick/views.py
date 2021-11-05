# -*- coding: utf-8 -*-
"""
    core.views
    ~~~~~~~~~~~~~~
    项目的演示代码.
    :copyright: (c) 2019-10-08 by datochan.
"""
from flask_quick import quick_flask


@quick_flask.route('/', methods=['GET', 'POST'])
def index():
    return 'Hello, It Works!'
