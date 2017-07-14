import cherrypy

class BaseService(object):

    exposed = True
    _cp_config = { 'tools.json_out.on': True }

    def DELETE(self):
        return {"status": 405, "message":"Method not implemented."}

    def GET(self):
        return {"status": 405, "message":"Method not implemented."}

    def HEAD(self):
        return {"status": 405, "message":"Method not implemented."}

    def POST(self):
        return {"status": 405, "message":"Method not implemented."}

    def PUT(self):
        return {"status": 405, "message":"Method not implemented."}


