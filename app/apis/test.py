"""
Test API using Test model
"""
from flask import Blueprint, jsonify
from flask import current_app as gapp
from flask_jwt_extended import jwt_required
from utils.permissions import permission_required, company_match
from app.apis.options import PATH_PREFIX, ERR_SOMETH
from app.models.test import (
    Test, TestSchema
)

test_api = Blueprint('test_api', __name__)

@test_api.route(PATH_PREFIX+'/hello', methods=["GET"])
@jwt_required
def api_test():
    """
    Test endpoint
    """
    return jsonify({'message': 'Hello world. You are authenticated'})

@test_api.route(PATH_PREFIX+'/path/<cuuid>/<juuid>/<appid>', methods=["GET"])
@permission_required('company:admin', 'job:admin')
@company_match
def get_path(cuuid, juuid, appid):
    """
    Checks various permissions and scopes
    """
    try:
        # Do soemthing with data
        gapp.logger.info(cuuid, juuid, appid)
        return jsonify({'message': 'Hello world. You have required roles.'})
    except Exception as e:
        gapp.logger.error(e)
        return jsonify({'msg': ERR_SOMETH}), 400

@test_api.route(PATH_PREFIX+'/all', methods=["GET"])
def get_all():
    """
    Checks various permissions and scopes
    """
    try:
        # Do soemthing with data
        all_tests = Test.query.all()
        result = TestSchema(many=True).dump(all_tests)
        return jsonify(result.data)
    except Exception as e:
        gapp.logger.error(e)
        return jsonify({'msg': ERR_SOMETH}), 400

