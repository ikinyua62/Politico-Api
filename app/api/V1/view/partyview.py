from flask import Flask, jsonify, request, make_response, Blueprint, Response
from app.api.v1.models.parties_model import Party


"""The below file reisters blueprints for the api"""
pt_v1 = Blueprint('v1', __name__, url_prefix='/api/v1')


"""This end point allow admin to delete a political party"""
@pt_v1.route('/editparties<party_id>', methods=['DELETE'])
def delete_a_party(self, party_id):
    Party().delete_party(party_id)
    return make_response(jsonify({
        'status': 'OK',
        'message': 'successfully deleted'
    }), 200)
