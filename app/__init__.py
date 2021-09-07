# -*- coding: utf-8 -*-
"""
    core
    ~~~~~~~~~~~~~~
    通用模块.

    :copyright: (c) 2019-10-08 by datochan.
"""


from flask import Blueprint

__app__ = Blueprint('app', __name__)

APP_MODULES = (
    {"entry": __app__},
)


from . import lib, views
