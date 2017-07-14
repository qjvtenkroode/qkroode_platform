import authentication.baseAuthentication as baseAuthentication

def test_validate_user():
    valid_user = baseAuthentication.validate_user('localhost','admin','changeme')
    assert valid_user == True
    invalid_user = baseAuthentication.validate_user('locahost','admin','changemenow')
    assert invalid_user == False

def test_add():
    pass

def test_delete():
    pass

def test_read_hashes():
    pass

def test_write_hashes():
    pass
