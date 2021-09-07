"""
    core.lib.bootstrap
    ~~~~~~~~~~~~~~
    项目的入口文件, 用来启动项目加载相应的模块.

    :copyright: (c) 2019-10-08 by datochan.
"""
from flask import Flask
from quick_flask import Configure

from .extensions import db, login_manager

DEFAULT_APP_NAME = 'python-flask-quick-start'
DEFAULT_APP_MODULES = ()


def create_app(config: Configure = None, modules=None):
    if modules is None:
        modules = DEFAULT_APP_MODULES

    app = Flask(DEFAULT_APP_NAME)

    if config is not None:
        app.config.from_object(config)
        config.init_app(app)

    # register module
    configure_modules(app, modules)
    configure_extensions(app)

    return app


def configure_extensions(app):
    # configure extensions
    db.init_app(app)
    login_manager.init_app(app)


def configure_modules(app, modules):
    for module in modules:
        app.register_blueprint(module.get("entry", None), url_prefix=module.get("prefix", None))
