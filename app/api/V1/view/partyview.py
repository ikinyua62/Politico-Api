from flask import Flask, jsonify, request, make_response, Blueprint, Response
from app.api.v1.models.parties_model import Party


"""The below file reisters blueprints for the api"""
pt_v1 = Blueprint('v1', __name__, url_prefix='/api/v1')


"""This end point allow admin to edit a party by creating a PATCH request on postman"""
@pt_v1.route('/parties/<int:party_id>/name', methods=['PUT'])
def edit_party_name(party_id):
    data = request.get_json
    party = Party().edit_party(party_id, data)
    return make_response(jsonify({
        'status': 'OK',
        'message': 'update successful',
        'parties': party
    })