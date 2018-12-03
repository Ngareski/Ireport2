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
        dosctring to post a users record
        """
        data = {
            'firstname': request.json.get('firstname', ""),
            'lastname' : request.json.get('lastname', ""),
            'othernames' :request.json.get('othernames', ""),
            'email' : request.json.get('email', ""),
            'phoneNumber' : request.json.get('phoneNumber', ""),
            'username' : request.json.get('username', ""),
            'registered' : datetime.datetime.utcnow()
        }
        self.db.save(data)

        return make_response(jsonify({
            "status" : 201,
            "data" : "Succesfuly created account"
        }), 201)

class UserGet(Resource):
    """
    docstring for a single red-flag
    """
    def __init__(self):
        self.db = UserModels()

    def get(self, user_id):
        """
        docstring to get a single user
        """    
        user = self.db.find(user_id)
        return make_response(jsonify({
            "status" :200,
            "data" : user
        }), 200)
             
    def delete(self, user_id):
        """
        docstring to delete a single user
        """
        user = self.db.find(user_id)
        self.db.delete(user)
        return make_response(jsonify({
            "status" : 200,
            "data" : "Succesfuly deleted user"
        }), 200)
    
    def put(self, user_id):
        """
        docstring to edit users entire record
        """
        user = self.db.find(user_id)

        if user:
            incident['firstname'] = request.json.get('firstname', incident[0]['firstname'])
            incident['lastname'] = request.json.get('lastname', incident[0]['lastname'])
            incident['othernames'] = request.json.get('othernames', incident[0]['othernames'])
            incident['othernames'] = request.json.get('othernames', incident[0]['othernames'])
            incident['phoneNumber'] = request.json.get('phoneNumber', incident[0]['phoneNumber'])
            incident['username'] = request.json.get('username', incident[0]['username'])
            return make_response(jsonify({
                "status" : 200,
                "data" : "succesfuly edited your record"
            }), 200)
        return make_response(jsonify({
            "status" : 404,
            "error" : "User records dont exist"
        }))

class UserEdit(Resource):
    """
    docstring to edit user data
    """
    def __init__(self):
        self.db = UserModels()

    def patch(self, user_id):
        """
        docstring to update user phone number
        """
        user = self.db.find(user_id)
        if user:
            user['phoneNumber'] = request.json.get('phoneNumber', user['phoneNumber'])
            return make_response(jsonify({
                "status" : 200,
                "data" : "Succefuly updated phone number"
            }), 200)
        return make_response(jsonify({
            "status" : 404,
            "error" : "user does not exist"
        }))







            
        
