import unittest
import json

from run import app

class TestRedFlag(unittest.TestCase):
    def setUp(self):
        """
        setting up the app for testing
        """
        app.testing = True
        self.app = app.test_client()
        self.data = {
            "id": 1,
            "createdOn" : "Tue, 27 Nov 2018 21:18:13 GMT",
            "createdBy" : "Ngare",
            'type' : 'red-flags',
            "location" : "kasarani",
            "status" : "UI",
            "images" : "",
            "videos" : "",
            "title" : "Police brutalityr",
            "comment" : "Police brutaluuubsudsidunidansid."
        }

    def test_red_flags_get(self):
        """
        test for get red flags endpoint
        """
        response = self.app.get("/api/v1/red-flags")
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 200)

    def test_redflag(self):
        """
        test to get a specified redflag
        """
        response = self.app.post("/api/v1/red-flags", headers={'Content-Type': 'application/json'}, data = json.dumps(self.data))
        response2 = self.app.get("/api/v1/red-flags/1")
        result = json.loads(response2.data)
        self.assertEqual(response2.status_code, 200)
    
    def test_redflags_post(self):
        """
        test for post a redflag
        """
        response = self.app.post("/api/v1/red-flags", headers={'Content-Type': 'application/json'}, data = json.dumps(self.data))
        result = json.loads(response.data)
        self.assertEqual(response.status_code, 201)

    def test_delete_redflag(self):
        """test to delete a specific redflag"""
        response = self.app.post("/api/v1/red-flags", headers={'Content-Type': 'application/json'}, data = json.dumps(self.data))
        response2 = self.app.delete("/api/v1/red-flags/1")
        result = json.loads(response2.data)
        self.assertEqual(response2.status_code, 200)

    def test_update_location(self):
        """
        Updates the loccation of a specified red-flag
        """
        response = self.app.post("/api/v1/red-flags/1/location", headers={'Content-Type': 'application/json'}, data = json.dumps(self.data))
        response2 = self.app.patch("/api/v1/red-flags/1/location", headers={'Content-Type': 'application/json'}, data = json.dumps({"location" : "Mwiki"}))
        result = json.loads(response2.data)
        self.assertEqual(response2.status_code, 200)

    def test_update_comment(self):
        """updates comment of a specified red-flag"""
        response = self.app.post("/api/v1/red-flags/1/comment", headers={'Content-Type': 'application/json'}, data = json.dumps(self.data))
        response2 = self.app.patch("/api/v1/red-flags/1/comment", headers={'Content-Type': 'application/json'}, data = json.dumps({"comment" : "Police brutality needes to stop"}))
        result = json.loads(response2.data)
        self.assertEqual(response2.status_code, 200) 

    

    
if __name__ == "__main__":
    unittest.main()