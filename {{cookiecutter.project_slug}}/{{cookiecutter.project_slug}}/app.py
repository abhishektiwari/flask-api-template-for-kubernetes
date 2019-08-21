"""
Your services
"""
import logging
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from {{cookiecutter.project_slug}}.extensions import (
    db,
    mg,
    ma
)

def create_app(config_name):
    """Creat app and return"""
    # Flask app
    app = Flask(__name__) # pylint: disable=invalid-name
    from {{cookiecutter.project_slug}}.config import config
    {{cookiecutter.project_slug}}.config.from_object(config[config_name])
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
        {{cookiecutter.project_slug}}.logger.setLevel(logging.INFO) # pylint: disable=no-member
    else:
        {{cookiecutter.project_slug}}.logger.setLevel(logging.ERROR) # pylint: disable=no-member

    # API blueprints, imported after OS.environ
    from {{cookiecutter.project_slug}}.apis.public import public_api
    {{cookiecutter.project_slug}}.register_blueprint(public_api)
    from {{cookiecutter.project_slug}}.apis.private import private_api
    {{cookiecutter.project_slug}}.register_blueprint(private_api)
    from {{cookiecutter.project_slug}}.apis.test import test_api
    {{cookiecutter.project_slug}}.register_blueprint(test_api)

    return app