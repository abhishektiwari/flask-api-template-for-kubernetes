"""
Your services
"""
import logging
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS

def create_app(config_name):
    """Creat app and return"""
    # Flask app
    app = Flask(__name__) # pylint: disable=invalid-name
    from app.config import config
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    # set up extensions
    # set up extensions
    from database import db
    db.init_app(app)
    from migrate import mg
    mg.init_app(app, db)
    from marsh import ma
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
    from app.apis.public import public_api
    app.register_blueprint(public_api)
    from app.apis.private import private_api
    app.register_blueprint(private_api)
    from app.apis.test import test_api
    app.register_blueprint(test_api)

    return app