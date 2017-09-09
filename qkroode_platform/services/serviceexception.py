
class ServiceException(Exception):
    """
    ServiceException class to wrap into the Flask Application
    and enable a better Exception handling for Services
    """

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        """ Returns the payload as a dictionary and adds message and status fields """
        retv = dict(self.payload or ())
        retv['message'] = self.message
        retv['status'] = self.status_code
        return retv
