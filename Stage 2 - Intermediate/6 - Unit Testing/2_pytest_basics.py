import pytest
from calculator import add, subtract, multiply, divide, calculate_discount, is_even, get_grade

# pytest is simpler than unittest - no class or self needed
# just write functions that start with "test_" and use plain assert
# run with: pytest 2_pytest_basics.py  or  pytest -v  for detailed output


# pytest uses plain assert - much simpler than self.assertEqual
def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(10, 3) == 7


def test_multiply():
    assert multiply(4, 5) == 20


def test_divide():
    assert divide(10, 2) == 5.0


def test_is_even():
    # multiple assertions in one test are fine for closely related checks
    assert is_even(4) is True
    assert is_even(3) is False


# pytest.raises() - test that the correct exception is raised
# the test PASSES only if ZeroDivisionError is raised inside the 'with' block
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


# discount > 100 is invalid, should raise ValueError
def test_invalid_discount():
    with pytest.raises(ValueError):
        calculate_discount(100, 150)


# fixtures - functions decorated with @pytest.fixture that return test data
# pytest automatically passes the fixture's return value to any test that names it as a parameter
@pytest.fixture
def sample_prices():
    # this data is shared across any test that uses the 'sample_prices' parameter
    return {"laptop": 50000, "phone": 30000, "tablet": 20000}


@pytest.fixture
def student():
    return {"name": "Jay", "marks": 85}


# 'sample_prices' here is not an argument we pass - pytest injects the fixture automatically
def test_discount_on_laptop(sample_prices):
    result = calculate_discount(sample_prices["laptop"], 10)
    assert result == 45000.0


def test_discount_on_phone(sample_prices):
    result = calculate_discount(sample_prices["phone"], 20)
    assert result == 24000.0


# pytest injects the 'student' fixture automatically
def test_student_grade(student):
    grade = get_grade(student["marks"])
    assert grade == "B"


# parametrize - runs the SAME test function once for every row in the list
# avoids writing a separate test function for each input combination
# each row is: (a, b, expected)
@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5),
    (10, 20, 30),
    (0, 0, 0),
    (-5, 5, 0),
    (100, 200, 300),
])
def test_add_parametrize(a, b, expected):
    assert add(a, b) == expected


# pytest will run this 5 times, once per (marks, expected_grade) pair
@pytest.mark.parametrize("marks, expected_grade", [
    (95, "A"),
    (80, "B"),
    (65, "C"),
    (45, "D"),
    (20, "F"),
])
def test_get_grade_parametrize(marks, expected_grade):
    assert get_grade(marks) == expected_grade


@pytest.mark.parametrize("price, discount, expected", [
    (1000, 10, 900),
    (500, 20, 400),
    (200, 50, 100),
    (1000, 0, 1000),   # no discount
    (1000, 100, 0),    # full discount
])
def test_discount_parametrize(price, discount, expected):
    assert calculate_discount(price, discount) == expected
