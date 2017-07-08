import cherrypy
import json

from bson.objectid import ObjectId


class BaseService(object):

    exposed = True

    collection = None

    def DELETE(self):
        raise cherrypy.HTTPError(405, "Method not implemented.")

    def GET(self):
        raise cherrypy.HTTPError(405, "Method not implemented.")

    def HEAD(self):
        raise cherrypy.HTTPError(405, "Method not implemented.")

    def POST(self):
        raise cherrypy.HTTPError(405, "Method not implemented.")

    def PUT(self):
        raise cherrypy.HTTPError(405, "Method not implemented.")

    def get_id(self, id):
        # Convert string to MongoDB ObjectId and find document
        if not isinstance(id, ObjectId):
            id = ObjectId(id)
        document = self.collection.find_one({'_id': id})
        return document


class MongoDBEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        else:
            return json.JSONEncoder.default(self, o)

    def iterencode(self, value):
        # Adapted from cherrypy/_cpcompat.py
        for chunk in super(MongoDBEncoder, self).iterencode(value):
            yield chunk.encode("utf-8")

json_encoder = MongoDBEncoder()


def json_handler(*args, **kwargs):
    # Adapted from cherrypy/lib/jsontools.py
    value = cherrypy.serving.request._json_inner_handler(*args, **kwargs)
    return json_encoder.iterencode(value)
