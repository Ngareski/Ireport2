from flask import Flask, Blueprint
from flask_restful import Api, Resource

from instance.config import app_config
from redflags.views import RedFlag, RedFlags, UpdateRedComment, UpdateRedLocation
from users.views import UsersReg


version2 = Blueprint('api', __name__, url_prefix='/api/v2')

api = Api(version2)

api.add_resource(RedFlags, '/red-flags')
api.add_resource(RedFlag, '/red-flags/<int:redflag_id>')
api.add_resource(UsersReg, '/users')
api.add_resource(UpdateRedComment, '/red-flags/<int:redflag_id>/comment')
api.add_resource(UpdateRedLocation, '/red-flags/<int:redflag_id>/location')