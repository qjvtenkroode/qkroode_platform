from flask import Flask, jsonify

from services.baseService import BaseService
from services.serviceException import ServiceException

app = Flask(__name__)
@app.errorhandler(ServiceException)
def handle_serviceexception(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
    
app.add_url_rule('/services/', view_func=BaseService.as_view('services'))
