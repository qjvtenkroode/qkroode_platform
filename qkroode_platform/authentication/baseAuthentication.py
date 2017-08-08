import argparse
import getpass
import hashlib
import json

import sys

PASSWD_FILE = './etc/passwd'


def validate_user(real, username, password):
    pwhash = hashlib.sha512(password).hexdigest()
    hashes = read_hashes(PASSWD_FILE)
    if(pwhash == hashes.get(username, None)):
        return True
    else:
        return False

def add(username, password=None):
    if password is None:
        password = getpass.getpass('Password?: ')
        if not password:
            print('no password entered')
            return False
    pwhash = hashlib.sha512(password).hexdigest()
    data = {username: pwhash}
    new_hashes = read_hashes(PASSWD_FILE)
    if not new_hashes:
        new_hashes = data
    else:
        new_hashes.update(data)
    if write_hashes(PASSWD_FILE, new_hashes):
        return True
    else:
        return False

def delete(username):
    hashes = read_hashes(PASSWD_FILE)
    if not hashes:
        return False
    else:
        try:
            hashes.pop(username)
            write_hashes(PASSWD_FILE, hashes)
            return True
        except:
            return False

def read_hashes(conf):
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
    with open(conf, 'w') as json_hashes:
        try:
            json_hashes.write(json.dumps(hashes))
            return True
        except:
            return False

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate or delete an entry in passwd')
    parser.add_argument('username', metavar='username', nargs=1,
                        help='username of the affected user')
    parser.add_argument('--add', action='store_true',
                        help='add a user and hashed password')
    parser.add_argument('--del', dest='delete', action='store_true',
                        help='remove a user and hashed password')
    args = parser.parse_args()
    if(args.add):
        add(args.username[0])
    elif(args.delete):
        delete(args.username[0])
    else:
        print('Something went wrong..')
