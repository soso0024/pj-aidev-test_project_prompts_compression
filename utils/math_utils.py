"""
Mathematical utility functions. module provides basic mathematical operations additional safety features
"""

def add(a, b):
    """
    Add two numbers together Args : a : First number b : Second number Returns : sum of a and
    """
    return a + b


def multiply(a, b):
    """
    Multiply two numbers together Args : a : First number b : Second number Returns : product of a and
    """
    return a * b


def safe_divide(a, b):
    """
    Safely divide two numbers handling division by zero Args : a : Numerator b : Denominator Returns : result of a / b, or None if b is
    """
    if b == 0:
        return None
    return a / b
