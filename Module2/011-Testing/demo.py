# Testing 

# Pytest used as our testing platform
# pip install pytest

# When testing files ensure the file is called test_filename.py 
# for pytest to read - `pytest test_filename.py`

# Basic Test
def func(num):
    return num * 2

def test_answer():
    assert func(6) == 10

# Testing a function
def f():
    return 3

def test_function():
    assert f() == 4

# test-double.py
import double

def test_answer():
    assert double.func(6) == 10

# double.py

def func(num):
    return num * 2