"""
Public APIs
"""
from flask import Blueprint
from flask import jsonify
from flask import current_app as gapp
from app.apis.options import PATH_PREFIX

public_api = Blueprint('public_api', __name__) # pylint: disable=invalid-name

@public_api.route(PATH_PREFIX, methods=["GET"])
def index():
    """
    Index for this app
    """
    gapp.logger.info("Called index")
    return jsonify({'api': 'Your Services'})

@public_api.route(PATH_PREFIX+'/public', methods=["GET"])
def api_public():
    """
    Public endpoint
    """
    return jsonify({'message': 'Hello from a public endpoint!'})
