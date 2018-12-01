from flask_restful import Resource
from flask import jsonify, make_response, request, abort, Blueprint
from .models import RedFlagModels

import datetime

class RedFlags(Resource):
    """
    docstring for all redflags
    """
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
            "data" : success_msg
        }), 201)
