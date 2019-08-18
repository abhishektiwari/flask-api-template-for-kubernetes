"""
Test API using Test model
"""
from flask import Blueprint, jsonify, request
from flask import current_app as gapp
from flask_jwt_extended import (
    jwt_required,
    get_jwt_claims
)
from utils.permissions import permission_required, company_match
from ..models.test import (
    Test, TestSchema
)
from app.apis.options import PATH_PREFIX, ERR_INCORR, ERR_MISSIN, ERR_SOMETH, ERR_UNAUTH

test_api = Blueprint('test_api', __name__) # pylint: disable=invalid-name

@test_api.route(PATH_PREFIX+'/hello', methods=["GET"])
@jwt_required
def api_test():
    """
    Test endpoint
    """
    return jsonify({'message': 'Hello world. You are authenticated'})

@test_api.route(PATH_PREFIX+'/all/<cuuid>/<juuid>/<appid>', methods=["GET"])
@permission_required('company:admin', 'job:admin')
@company_match
def get_test(cuuid, juuid, appid):
    try:
        # Do soemthing with data
        gapp.logger.info(cuuid, juuid, appid)
        return jsonify({'message': 'Hello world. You have required roles.'})
    except Exception as e:
        gapp.logger.error(e)
        return jsonify({'msg': ERR_SOMETH}), 400