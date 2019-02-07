from flask import Flask, jsonify, request, make_response, Blueprint, Response
from app.api.v1.models.parties_model import Party


"""The below file reisters blueprints for the api"""
pt_v1 = Blueprint('v1', __name__, url_prefix='/api/v1')

"""This end point allows uadmin to create a new political party"""
@pt_v1.route('/parties', methods=['POST'])
def create__a_party():
    data = request.get_json()
    name = data['name']
    hqAddress = data['hqAddress']
    logoUrl = data['logoUrl']
    party = Party().create_party(name, hqAddress, logoUrl)
    return make_response(jsonify({
        "data": party,
        "status": 201,
        "msg": "created Successfully"

    }), 201)