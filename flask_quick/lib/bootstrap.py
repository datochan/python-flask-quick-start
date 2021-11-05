"""
    core.lib.bootstrap
    ~~~~~~~~~~~~~~
    项目的入口文件, 用来启动项目加载相应的模块.

    :copyright: (c) 2019-10-08 by datochan.
"""
from flask import Flask
from flask_quick import Configure

DEFAULT_APP_NAME = 'python-flask-quick-start'
DEFAULT_APP_MODULES = []


def create_app(config: Configure = None, extension=None, modules=None):
    if extension is None:
        extension = []

    if modules is None:
        modules = DEFAULT_APP_MODULES

    app = Flask(DEFAULT_APP_NAME)

    if config is not None:
        app.config.from_object(config)
        config.init_app(app)

    for ext in extension:
        ext.init_app(app)

    for module in modules:
        app.register_blueprint(module.get("entry", None), url_prefix=module.get("prefix", None))

    return app
