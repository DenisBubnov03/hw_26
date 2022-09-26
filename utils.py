from flask import Flask

from blueprint.errors import error_bp
from blueprint.loader import main_page, loader_blueprint
from blueprint.logging.auth import loader_blueprints


def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_page)
    app.register_blueprint(loader_blueprint)
    app.register_blueprint(loader_blueprints)
    app.register_blueprint(error_bp)
    app.secret_key = 'super secret key'
    return app