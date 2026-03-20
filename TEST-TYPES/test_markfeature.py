import pytest

@pytest.mark.smoke
def test_func1():
    print('hello this if fun-1')

@pytest.mark.sanity
def test_func2():
    print('hello this if fun-2')

@pytest.mark.smoke
def test_func3():
    print('hello this if fun-3')

@pytest.mark.sanity
def test_func4():
    print('hello this if fun-4')

@pytest.mark.smoke
def test_func5():
    print('hello this if fun-5')

@pytest.mark.sanity
def test_func6():
    print('hello this if fun-6')

