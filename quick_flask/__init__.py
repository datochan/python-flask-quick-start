from flask import Blueprint

quick_flask = Blueprint('quick_flask', __name__)

APP_MODULES = [
    {"entry": quick_flask},
]

from . import lib, views
