from flask_restful import Api, Resource
from flask import Blueprint

from instance.config import app_config
from app.api.v1.redflags.views import RedFlag, RedFlags, UpdateRedComment, UpdateRedLocation
from app.api.v1.users.views import UsersReg, UserLogin

version1 = Blueprint('api-v1', __name__, url_prefix= '/api/v1')
api = Api(version1)

api.add_resource(RedFlags, '/red-flags')
api.add_resource(RedFlag, '/red-flags/<int:redflag_id>')
api.add_resource(UpdateRedComment, '/red-flags/<int:redflag_id>/comment')
api.add_resource(UpdateRedLocation, '/red-flags/<int:redflag_id>/location')
api.add_resource(UsersReg, '/users')
api.add_resource(UserLogin, '/users/login')
