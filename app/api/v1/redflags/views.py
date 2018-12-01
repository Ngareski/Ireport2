from flask_restful import Resource
from flask import jsonify, make_response, request, abort, Blueprint
from .models import RedFlagModels

import datetime

class RedFlags(Resource):
    """
    docstring for all redflags
    """
