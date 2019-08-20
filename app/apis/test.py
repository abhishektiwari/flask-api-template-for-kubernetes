"""
Test API using Test model
"""
from flask import Blueprint, jsonify
from flask import current_app as gapp
from sqlalchemy.exc import IntegrityError
from webargs.flaskparser import use_kwargs
from app.apis.options import PATH_PREFIX, ERR_SOMETH
from app import db
from app.models.test import (
    Test, TestSchema
)

test_api = Blueprint('test_api', __name__)



@test_api.errorhandler(422)
@test_api.errorhandler(400)
def handle_error(err):
    """
    webargs attaches additional metadata, including
    validation errors, to the `data` attribute
    """
    return jsonify({
        'msg': err.data.get("messages", ["Invalid request."])
    }), err.code

@test_api.route(PATH_PREFIX+'/records', methods=["GET"])
def get_records():
    """
    Checks various permissions and scopes
    """
    try:
        # Do soemthing with data
        all_tests = Test.query.all()
        result = TestSchema(many=True, exclude=['id']).dump(all_tests)
        return jsonify(result.data), 200
    except Exception as e:
        gapp.logger.error(e)
        return jsonify({'msg': ERR_SOMETH}), 400

@test_api.route(PATH_PREFIX+'/records', methods=["POST"])
@use_kwargs(TestSchema(dump_only=['id']))
def add_record(name, email):
    """
    Add a new record
    """
    try:
        record = Test(name=name, email=email)
        db.session.add(record)
        db.session.commit()
        return jsonify({'msg': 'New record created'}), 200
    except IntegrityError as e:
        gapp.logger.error(e)
        return jsonify({'msg': 'Record already exists.'}), 400
