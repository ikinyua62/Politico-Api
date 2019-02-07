from flask import Flask, jsonify, request, make_response, Blueprint, Response
from app.api.v1.models.parties_model import Party


"""The below file reisters blueprints for the api"""
pt_v1 = Blueprint('v1', __name__, url_prefix='/api/v1')

"""This is the route allows user to retrieve one political party with specific party id"""


@pt_v1.route('/parties/<int:party_id>', methods=['GET'])
def get_by_id(party_id):
    party = Party().get_party_by_id(party_id)
    if party:
        return make_response(jsonify({
            'message': 'success',
            'Status': 200,
            'parties': party
        }), 200)
    return make_response(jsonify({
        'error': 404,
        'message': 'NOt found'
    }), 404)