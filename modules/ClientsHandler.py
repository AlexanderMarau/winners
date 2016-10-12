
import json
import settings

from bson import json_util
from bson.objectid import ObjectId
from tornado import ioloop,web

class ClientsHandler(web.RequestHandler):

    def get(self):
        clients = settings.db.clients.find()
        self.set_header("Content-Type", "application/json")
        self.write(json.dumps(list(clients),default=json_util.default))
  
    def post(self):
        story_data = json.loads(self.request.body)
        story_id = settings.db.clients.insert(story_data)
        print('story created with id ' + str(story_id))
        self.set_header("Content-Type", "application/json")
        self.set_status(201)