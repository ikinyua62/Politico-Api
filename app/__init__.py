from flask import Flask 
from flask import Blueprint 
from app.api.V1.view.partyview import pt_v1 as v1


def create_app():
    app=Flask(__name__)

    app=register_bueprint(v1)

    return app 

