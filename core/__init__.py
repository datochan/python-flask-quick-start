# -*- coding: utf-8 -*-
"""
    common
    ~~~~~~~~~~~~~~
    通用模块.

    :copyright: (c) 2019-10-08 by datochan.
"""


from flask import Blueprint

__core__ = Blueprint('core', __name__)

APP_MODULES = (
    {"entry": __core__},
)


from . import lib, views
