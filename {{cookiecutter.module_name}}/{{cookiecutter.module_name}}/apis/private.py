"""
Private APIs
"""
from flask import Blueprint
from flask import jsonify
from flask_jwt_extended import jwt_required
from {{cookiecutter.module_name}}.apis.options import PATH_PREFIX

private_api = Blueprint('private_api', __name__) # pylint: disable=invalid-name

@private_api.route(PATH_PREFIX+'/private', methods=["GET"])
@jwt_required
def api_private():
    """
    Private endpoint
    """
    return jsonify({'message': 'All good. You are authenticated'})
