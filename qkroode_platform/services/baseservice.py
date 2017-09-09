from flask.views import MethodView

from qkroode_platform.services.serviceexception import ServiceException
from qkroode_platform.authentication.baseauthentication import requires_auth

class BaseService(MethodView):
    """ A BaseService template for creating API endpoints """

    @requires_auth
    @classmethod
    def delete(cls):
        """ The HTTP DELETE method """
        raise ServiceException('Method not implemented.', status_code=501)

    @requires_auth
    @classmethod
    def get(cls):
        """ The HTTP GET method """
        raise ServiceException('Method not implemented.', status_code=501)

    @requires_auth
    @classmethod
    def head(cls):
        """ The HTTP HEAD method """
        raise ServiceException('Method not implemented.', status_code=501)

    @requires_auth
    @classmethod
    def post(cls):
        """ The HTTP POST method """
        raise ServiceException('Method not implemented.', status_code=501)

    @requires_auth
    @classmethod
    def put(cls):
        """ The HTTP PUT method """
        raise ServiceException('Method not implemented.', status_code=501)
