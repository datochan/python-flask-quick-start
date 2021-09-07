from quick_flask import APP_MODULES
from app.api_1_0 import __api_1_0

DEMO_MODULES = APP_MODULES + [
    {"entry": __api_1_0, "prefix": "/api/v1.0"}
]