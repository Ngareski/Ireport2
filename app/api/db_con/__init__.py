from flask import FLask, Blueprint

from instance import app_config

def create_app():
    app = Flask(__name__)

    from .api.v1 import version1 as v1
    app.register_blueprint(v1)

    from .api.v2 import version2 as v2
    app.register_blueprint(v2)

    return app