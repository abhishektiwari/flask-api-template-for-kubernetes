"""
Your services
"""
import logging
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from {{cookiecutter.module_name}}.extensions import (
    db,
    mg,
    ma
)

def create_app(config_name):
    """Creat app and return"""
    # Flask app
    app = Flask(__name__) # pylint: disable=invalid-name
    from {{cookiecutter.module_name}}.config import config
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # set up extensions
    # set up extensions
    db.init_app(app)
    mg.init_app(app, db)
    ma.init_app(app)

    # Setup the Flask-JWT-Extended extension and CORS
    JWTManager(app)
    CORS(app, resources={r"/{{ cookiecutter.api_prefix}}/*": {"origins": "*"}})

    # Add logger
    if config_name == 'development' or config_name == 'default':
        app.logger.setLevel(logging.INFO) # pylint: disable=no-member
    else:
        app.logger.setLevel(logging.ERROR) # pylint: disable=no-member

    # API blueprints, imported after OS.environ
    from {{cookiecutter.module_name}}.apis.public import public_api
    app.register_blueprint(public_api)
    from {{cookiecutter.module_name}}.apis.private import private_api
    app.register_blueprint(private_api)
    from {{cookiecutter.module_name}}.apis.test import test_api
    app.register_blueprint(test_api)

    return app