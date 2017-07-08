import cherrypy
import os

import authentication.baseAuthentication
import services.baseService

if __name__ == '__main__':
    cherrypy.tree.mount(
        None, '/', {
            '/': {
                'request.dispatch': cherrypy.dispatch.Dispatcher(),
                'tools.auth_basic.on': True,
                'tools.auth_basic.realm': 'localhost',
                'tools.auth_basic.checkpassword': authentication.baseAuthentication.validate_user,
            }
        }
    )
    cherrypy.tree.mount(
        services.baseService.BaseService(), '/api', {
            '/': {
                'request.dispatch': cherrypy.dispatch.MethodDispatcher(),
                'tools.auth_basic.on': True,
                'tools.auth_basic.realm': 'localhost',
                'tools.auth_basic.checkpassword': authentication.baseAuthentication.validate_user
            }
        }
    )
    cherrypy.config.update({'engine.autoreload.on': True})

    cherrypy.engine.start()
    cherrypy.engine.block()
