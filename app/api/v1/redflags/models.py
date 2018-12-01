
from flask import jsonify, make_response, request, abort, Blueprint
incidents = []

class RedFlagModels():

    def __init__(self):
        self.db = incidents

    def save(self, data):
        data['id'] = len(self.db) + 1

        self.db.append(data)
    
    def find(self, id):
        for incident in self.db:
            if incident['id'] == id:
                return incident
        
    def delete(self, incident):
        self.db.remove(incident)


    def get_all(self):
        return self.db


    def edit_comment(self,id):
        pass
          
