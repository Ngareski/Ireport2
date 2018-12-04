
from flask import jsonify, make_response, request, abort, Blueprint
users = []

class UserModels():

    def __init__(self):
        self.db = users

    def save(self, data):
        data['id'] = len(self.db) + 1

        self.db.append(data)

    def find(self, id):
        for user in self.db:
            if user['id'] == id:
                return user

    def delete(self, user):
        self.db.remove(user)


    def get_all(self):
        return self.db


    def edit_comment(self,id):
        pass
