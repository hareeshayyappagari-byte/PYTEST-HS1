import pytest, sys
from users import users,get_user,remove_user,add_user

def test_user_added(user_data):
    user_name, pwd = user_data
    assert user_name in users


def test_pwd_added(user_data):
    user_name, pwd = user_data
    assert get_user(user_name) == pwd


@pytest.mark.parametrize('username,pwd', [
    ("harish@1",'pwd-1'),
    ("harish@2",'pwd-2'),
    ("harish@3",'pwd-3'),
    ("harish@4",'pwd-4')
])
def test_multiple_inputs(username,pwd):
    # remove_user(username)
    add_user(username,pwd)
    print(f'test user {username}')
    assert get_user(username) == pwd
    remove_user(username)


@pytest.mark.skip(reason="<< practicing skip in pytest >>")
def test_sk_01():
    assert "hari" in 'harish'


@pytest.mark.skipif(sys.platform == 'win32', reason="Windows only")
def test_skif():
    assert "hari" in 'harish'


@pytest.mark.xfail(reason="<< practicing xfail in pytest >>")
def test_xfail():
    assert True



