from flask_restful import Resource
from flask import jsonify, make_response, request, abort, Blueprint
from .models import UserModels
import datetime

class UsersReg(Resource):
    """
    docstring for get all userss
    """
    def __init__(self):
        self.db = UserModels()

    def get(self):
        self.db.get_all()
        return make_response(jsonify({
            "status" : 200,
            "data" : self.db.get_all()
        }), 200)

    def post(self):
        """
        dosctring to create a users record
        """

        data = {

            'firstname': request.json.get('firstname', ""),
            'lastname' : request.json.get('lastname', ""),
            'othernames' :request.json.get('othernames', ""),
            'email' : request.json.get('email', ""),
            'phoneNumber' : request.json.get('phoneNumber', ""),
            'username' : request.json.get('username', ""),
            'registered' : datetime.datetime.utcnow(),
            'password' : request.json.get('password', ""),
            'confirmpassword' : request.json.get('password',"")
        }
        self.db.save(data)

        return make_response(jsonify({
            "status" : 201,
            "data" : "Succesfuly created account"
        }), 201)

class  UserLogin(Resource):
    """docstring foor user login  ."""
    def __init__(self):
        self.db = UserModels()

    def post(self):
        data = {
        'email' : request.json.get('email', ""),
        'password' : request.json.get('password', "")
        }
        self.db.save(data)

        return make_response(jsonify({
            "status" : 200,
            "data" : "Logged in"
        }),200)
