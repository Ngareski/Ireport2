from flask_restful import Resource
from flask import jsonify, make_response, request, abort, Blueprint

import datetime

users = []

class UsersReg(Resource):

    def __init__(self):
        self.db = users
        
        if len(users) == 0:
            self.id = len(users) +1
        else:
            self.id = users[-1]['id'] + 1
    def get(self):
    
        return make_response(jsonify({
            "status" : 200,
            "data" : self.db
        }), 200)

    def post(self):

        data = {
            "id" : self.id,
            "firstname" : request.json.get('firstname', ""),
            "lastname" : request.json.get('lastname', ""),
            "othernames" : request.json.get('othernames', ""),
            "email" : request.json.get('email', ""),
            "phonenumber" : request.json.get('phonenumber', ""),
            "username" : request.json.get('username', ""),
            "registered" :datetime.datetime.utcnow(),
            
        }

        self.db.append(data)

        success_msg = {
            'id' : self.id,
            'message': 'created user'
        }

        return make_response(jsonify({
            "status" : 201,
            "data" : success_msg
        }), 201)
