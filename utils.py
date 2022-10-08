import os
from hashlib import md5

from flask import Flask

from blueprint.errors import error_bp
from blueprint.loader import main_page, loader_blueprint
from blueprint.logging.auth import loader_blueprints
DB_USER = os.getenv('docker_app')
DB_PASSWORD = os.getenv('docker_app')
DB_NAME = os.getenv('docker_app')

def create_app():
    app = Flask(__name__)
    app.config["JSON_AS_ASCII"] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{DB_USER}:{DB_PASSWORD}@postgres/{DB_NAME}'
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.register_blueprint(main_page)
    app.register_blueprint(loader_blueprint)
    app.register_blueprint(loader_blueprints)
    app.register_blueprint(error_bp)
    app.secret_key = 'super secret key'
    return app
