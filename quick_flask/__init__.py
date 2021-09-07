from flask import Blueprint

quick_flask = Blueprint('quick_flask', __name__)

from . import lib, views
