import pytest

from users import add_user,remove_user

@pytest.fixture
def user_data():
    u_name,pwd = 'harish','harish@123'
    # remove_user(u_name)
    add_user(u_name,pwd)
    print('data added successfully')
    yield (u_name,pwd)
    remove_user(u_name)
    print('data removed successfully')
