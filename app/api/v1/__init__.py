from flask_restful import Api, Resource
from flask import Blueprint

from instance.config import app_config
from redflags.views import RedFlag, RedFlags, UpdateRedComment, UpdateRedLocation
from users.views import UsersReg

version1 = Blueprint('api-v1', __name__, url_prefix= '/api/v1')
api = Api(version1)

api.add_resource(RedFlags, '/red-flags')
api.add_resource(RedFlag, '/red-flags/<int:redflag_id>')
api.add_resource(UsersReg, '/users')
api.add_resource(UpdateRedComment, '/red-flags/<int:redflag_id>/comment')
api.add_resource(UpdateRedLocation, '/red-flags/<int:redflag_id>/location')
