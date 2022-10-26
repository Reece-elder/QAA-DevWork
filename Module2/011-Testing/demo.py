# Testing 

# Pytest used as our testing platform
# pip install pytest

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