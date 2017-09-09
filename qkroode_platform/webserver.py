from flask import Flask, jsonify

from qkroode_platform.services.baseService import BaseService
from qkroode_platform.services.serviceException import ServiceException

PLATFORM = Flask(__name__)
@PLATFORM.errorhandler(ServiceException)
def handle_serviceexception(error):
    """ Deal with Exceptions in a Service in a nicer manner """
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

PLATFORM.add_url_rule('/services/', view_func=BaseService.as_view('services'))
