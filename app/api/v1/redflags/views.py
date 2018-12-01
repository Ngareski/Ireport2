from flask_restful import Resource
from flask import jsonify, make_response, request, abort, Blueprint
from .models import RedFlagModels

import datetime

class RedFlags(Resource):
    """
    docstring for all redflags
    """
    def __init__(self):
        self.db = RedFlagModels()
    
    def get(self):
        self.db.get_all()

        return make_response(jsonify({
            "status" : 200,
            "data" : self.db.get_all()
        }), 200)
        
        
    def post(self):
        
        data = {
            'createdOn' : datetime.datetime.utcnow(),
            'createdBy' : request.json['createdBy'],
            'type' : 'red-flags',
            'location' : request.json.get('location', ""),
            'status' : "draft",
            'images' : request.json.get('images', ""),
            'videos' : request.json.get('videos', ""),
            'title' : request.json['title'],
            'comment' : request.json.get('comment', "")
        }
        self.db.save(data)
        
        success_msg = {
            "message" : "Created red-flag record"
        }

        return make_response(jsonify({
            "status" : 201,
            "data" : success_msg}), 201)

class RedFlag(Resource):
    """
    docstring for a single red-flag
    """
    def __init__(self):
        self.db = RedFlagModels()

    def get(self, redflag_id):
         
        incident = self.db.find(redflag_id)
        return make_response(jsonify({
            "status" :200,
            "data" : incident
        }), 200)
        

    def delete(self, redflag_id):
        incident = self.db.find(redflag_id)

        self.db.delete(incident)
        
        success_msg = {
                'message' : " Red-flag record has been deleted"
            }

        return make_response(jsonify({
            "status" : 200,
            "data" : success_msg
        }), 200)
        
    def put(self, redflag_id):
        incident = self.db.find(redflag_id)

        if incident:
            incident['createdBy'] = request.json.get('createdBy', incident[0]['createdBy'])
            incident['location'] = request.json.get('location', incident[0]['location'])
            incident['images'] = request.json.get('images', incident[0]['images'])
            incident['videos'] = request.json.get('videos', incident[0]['videos'])
            incident['title'] = request.json.get('title', incident[0]['title'])
            incident['comment'] = request.json.get('comment', incident[0]['comment'])
            success_msg = {
                    "message" : "Red- flag has been updated"
            }

            return make_response(jsonify({
                "status" : 200,
                "data" : success_msg
            }), 200)
        return make_response(jsonify({
            "status" : 404,
            "error" : "Red-flag does not exist"
        }), 404)

        }), 201)

class UpdateRedLocation(Resource):
    """
    docstring to update a red-flag location
    """
    def __init__(self):
        self.db = RedFlagModels()

    def patch(self, redflag_id):
        incident = self.db.find(redflag_id)
        incident = self.db.find(redflag_id)

        if incident:
            incident['location'] = request.json.get('location', incident['location'])
            success_msg = {
                        "message" : "Updated red-flag record's location"
                    }

            return make_response(jsonify({
                    "status" : 200,
                    "data" : success_msg
                }), 200)
        return make_response(jsonify({
        "status" : 404,
        "error" : "Red-flag does not exist"
        }), 404)

class UpdateRedComment(Resource):
    """
    docstring to update a red-flag ccomment
    """
    def __init__(self):
            self.db = RedFlagModels()

    def patch(self, redflag_id):
        incident = self.db.find(redflag_id)
        incident = self.db.find(redflag_id)

        if incident:
            incident['comment'] = request.json.get('comment', incident['comment'])
            success_msg = {
                            "message" : "Updated red-flag record's comment"
                    }

            return make_response(jsonify({
                    "status" : 200,
                    "data" : success_msg
                }), 200)

        return make_response(jsonify({
            "status" : 404,
            "error" : "Red-flag does not exist"
        }), 404)
        
            self.db = RedFlagModels()

