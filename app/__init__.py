import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import config

# Import models so that they are registered with SQLAlchemy
from . import models

# Flask extensions
db = SQLAlchemy()


def create_app(config_name=None):
    if config_name is None:
        config_name = os.environ.get('FLACK_CONFIG', 'development')
    app_obj = Flask(__name__)
    app_obj.config.from_object(config[config_name])

    # Initialize flask extensions
    db.init_app(app_obj)

    # Register web application routes
    from .app import main as main_blueprint
    app_obj.register_blueprint(main_blueprint)

    # Register API routes
    from .api import api as api_blueprint
    app_obj.register_blueprint(api_blueprint, url_prefix='/api')

    return app_obj
