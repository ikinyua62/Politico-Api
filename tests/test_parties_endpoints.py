import json
import unittest
import pytest
from app import create_app

class TestParties(unittest.TestCase):

    def setUp(self):
        self.app =create_app()
        self.client =self.app.test_client()
        self.dummy_data= {
            "name" : "office of the President " ,
            "candidate_id" :"P2018S" ,
            "date_created" : "00/00/0000"
        }
    def post(self, path = 'api/v1/party' ):
        """Creating a base post response with some dummy data """
        response= self.client.post(path='api/vi/offices',data=json.dumps(self.dummy_data),content_type='application/json')
        return response

    def test_create_party(self):
        """ Tests create party"""
        respo = self.post()
        result = json.loads(respo.data.decode())
        respo2= self.client.post(path="api/v1/party" ,data=json.dumps(self.dummy_data),content_type='application/json')
        result2 = json.loads(respo.data.decode())
        self.assertTrue(respo.status_code, 201)

    def test_get_all_parties(self):
        respo = self.post() 
        result = json.loads(respo.data.decode())
        respo2= self.client.post(path="api/v1/party" ,data=json.dumps(self.dummy_data),content_type='application/json')
        result2 = json.loads(respo.data.decode())
        self.assertTrue(respo.status_code,200)

    def test_get_specific_party(self):    
        respo = self.post()
        result = json.loads(respo.data.decode())
        respo2= self.client.post(path="api/v1/party{}party_id" ,data=json.dumps(self.dummy_data),content_type='application/json')
        result2 = json.loads(respo.data.decode())
        self.assertTrue(respo.status_code, 200)
