def add(a, b):
    try:
        return a + b
    except TypeError:
        raise TypeError("Both arguments must be numbers")

def subtract(a, b):
    try:
        return a - b
    except TypeError:
        raise TypeError("Both arguments must be numbers")

def multiply(a, b):
    try:
        return a * b
    except TypeError:
        raise TypeError("Both arguments must be numbers")

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        raise ZeroDivisionError("Cannot divide by zero")
    except TypeError:
        raise TypeError("Both arguments must be numbers")