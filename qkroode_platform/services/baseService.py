from flask.views import MethodView

from qkroode_platform.services.serviceException import ServiceException
from qkroode_platform.authentication.baseAuthentication import requires_auth

class BaseService(MethodView):

    @requires_auth
    def delete(self):
        raise ServiceException("Method not implemented.", status_code=501)

    @requires_auth
    def get(self):
        raise ServiceException("Method not implemented.", status_code=501)

    @requires_auth
    def head(self):
        raise ServiceException("Method not implemented.", status_code=501)

    @requires_auth
    def post(self):
        raise ServiceException("Method not implemented.", status_code=501)

    @requires_auth
    def put(self):
        raise ServiceException("Method not implemented.", status_code=501)

