import argparse
import getpass
import hashlib
import json
from functools import wraps
from flask import request, jsonify

PASSWD_FILE = './etc/passwd'


def validate_user(username, password):
    """ Validates a hash with a stored user hash """
    pwhash = hashlib.sha512(password).hexdigest()
    hashes = read_hashes(PASSWD_FILE)
    return bool(pwhash == hashes.get(username, None))

def add(username, password=None):
    """ Adds a user and hash to the hash store """
    if password is None: # pragma: no cover
        password = getpass.getpass('Password?: ')
        if not password:
            print 'no password entered'
            return False
    pwhash = hashlib.sha512(password).hexdigest()
    data = {username: pwhash}
    new_hashes = read_hashes(PASSWD_FILE)
    if not new_hashes: # pragma: no cover
        new_hashes = data
    else:
        new_hashes.update(data)
    return bool(write_hashes(PASSWD_FILE, new_hashes))

def delete(username):
    """ Deletes a user and hash from the hash store """
    hashes = read_hashes(PASSWD_FILE)
    if not hashes: # pragma: no cover
        return False
    else:
        try:
            hashes.pop(username)
            write_hashes(PASSWD_FILE, hashes)
            return True
        except:
            return False

def read_hashes(conf):
    """ Reads all users and corresponding hashes from the hash store into memory """
    try:
        json_hashes = open(conf, 'r')
        try:
            hashes = json.load(json_hashes)
        except:
            hashes = []
        json_hashes.close()
        return hashes
    except IOError:
        json_hashes = open(conf, 'w')
        hashes = []
        json_hashes.close()
        return hashes

def write_hashes(conf, hashes):
    """ Writes all in-memory hashes to the hash store """
    with open(conf, 'w') as json_hashes:
        try:
            json_hashes.write(json.dumps(hashes))
            return True
        except IOError:
            return False

def authenticate():
    """ Method which tags the request to enforce authentication """
    message = {'message': "Unauthorized access attempt."}
    resp = jsonify(message)
    resp.mimetype = 'application/json'
    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="Login Required"'
    return resp

def requires_auth(func):
    """ wrapper used to require authentication before using a function """
    @wraps(func)
    def decorated(*args, **kwargs):
        """ Decorates the request with an authorization tag """
        auth = request.authorization
        if not auth or not validate_user(auth.username, auth.password):
            return authenticate()
        return func(*args, **kwargs)
    return decorated

if __name__ == '__main__': # pragma: no cover
    PARSER = argparse.ArgumentParser(description='Generate or delete an entry in passwd')
    PARSER.add_argument('username', metavar='username', nargs=1,
                        help='username of the affected user')
    PARSER.add_argument('--add', action='store_true',
                        help='add a user and hashed password')
    PARSER.add_argument('--del', dest='delete', action='store_true',
                        help='remove a user and hashed password')
    ARGS = PARSER.parse_args()
    if ARGS.add:
        add(ARGS.username[0])
    elif ARGS.delete:
        delete(ARGS.username[0])
    else:
        print 'Something went wrong..'
