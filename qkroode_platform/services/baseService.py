from flask.views import MethodView

from serviceException import ServiceException

class BaseService(MethodView):

    def delete(self):
        raise ServiceException("Method not implemented.", status_code=501)

    def get(self):
        raise ServiceException("Method not implemented.", status_code=501)

    def head(self):
        raise ServiceException("Method not implemented.", status_code=501)

    def post(self):
        raise ServiceException("Method not implemented.", status_code=501)

    def put(self):
        raise ServiceException("Method not implemented.", status_code=501)

