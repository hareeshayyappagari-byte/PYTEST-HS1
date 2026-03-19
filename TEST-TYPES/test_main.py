import pytest

from main import add,divide,subtract,multiply

def test_add(): # Unit Testing - testing the single function
    res = add(3,3)
    assert res == 6



def test_devide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(3,0)



# integration test - check multiple functions working or not
def test_intigration():
    assert add(3,3) == multiply(3,2)

def test_add_and_multiply():
    res = multiply(add(1,3),2)
    assert res == 8


def test_three():
    res = multiply(add(1,3),subtract(5,add(1,2))) # 4    2
    print(res)
    assert res == 8


