# pip install pylint
# pylint demo.py
from math import sqrt

def square_times_two(num):
    return sqrt(num) * 2

# Example Code

# coolVariableName="cool value"
# def printtext(x):
#    return f"Text added is {x}"
# print(printtext('Hello'))
# rated as 0 / 10

# Comments are for commenting on specific parts of code if needed
"""
3 Quote marks together and used for convention
A docstring is a String with 3 quote marks that is not assigned a value
Module docstring, sits at the top of the file and tells everyone what the file does
"""
COOL_VAR = "cool value"

def printtext(text):
    """ Tells you what the function does """
    return f"Text added is {text}"

print(printtext('Hello'))
# Code is rated 10 / 10 


# We can use pylint to tell us how bad our code is
# pylint <name of file>

# Exercise - use pylint on your dice roller exercise, aim to get a 10 / 10 score 