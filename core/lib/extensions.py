"""
    core.lib.extensions
    ~~~~~~~~~~~~~~
    项目的扩展模块, 如果有新的扩展可在这里添加集中导入.

    :copyright: (c) 2019-10-08 by datochan.
"""
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

__all__ = ['db', 'login_manager']

db = SQLAlchemy()
login_manager = LoginManager()