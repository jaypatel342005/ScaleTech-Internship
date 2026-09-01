def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("cannot divide by zero")
    return a / b


def calculate_discount(price, discount):
    if discount < 0 or discount > 100:
        raise ValueError("discount must be between 0 and 100")
    return price - (price * discount / 100)


def is_even(n):
    return n % 2 == 0


def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "F"
