import os

import authentication.baseAuthentication as baseAuthentication

def test_validate_user():
    valid_user = baseAuthentication.validate_user('admin','changeme')
    assert valid_user == True
    invalid_user = baseAuthentication.validate_user('admin','changemenow')
    assert invalid_user == False

def test_add():
    test_user = baseAuthentication.add('test_user', 'blabla')
    assert test_user == True

def test_delete():
    deleted_user = baseAuthentication.delete('test_user')
    assert deleted_user == True
    failed_deleted_user = baseAuthentication.delete('not_existing')
    assert failed_deleted_user == False

def test_read_hashes():
    empty_hashes = baseAuthentication.read_hashes('./tests/empty_test_hashes.json')
    assert empty_hashes == []
    hashes = baseAuthentication.read_hashes('./tests/test_hashes.json')
    assert len(hashes) == 2

def test_write_hashes():
    test_hashes = {'user': 'blabla'}
    write_hashes = baseAuthentication.write_hashes('./tests/write_hashes.json', test_hashes)
    assert write_hashes == True
    try:
        os.remove('./tests/write_hashes.json')
    except:
        return False
