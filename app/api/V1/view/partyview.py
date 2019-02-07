from flask import Flask, jsonify, request, make_response, Blueprint, Response
from app.api.v1.models.parties_model import Party


"""The below file reisters blueprints for the api"""
pt_v1 = Blueprint('v1', __name__, url_prefix='/api/v1')


"""This is the route for retrieving all political parties."""


@pt_v1.route('/parties', methods=['GET'])
def get_all_parties():
    parties = Party().get_all()
    if parties:
        return make_response(jsonify({
            'msg': 'success',
            'parties': parties
        }))
