import unittest
from calculator import add, subtract, multiply, divide, calculate_discount, is_even, get_grade

# unittest is python's built-in testing framework - no installation needed
# every test class must inherit from unittest.TestCase
# every test method must start with "test_" so unittest can find it


class TestCalculator(unittest.TestCase):

    # assertEqual - checks if two values are exactly equal
    def test_add(self):
        self.assertEqual(add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(multiply(4, 5), 20)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5.0)

    # assertNotEqual - checks that two values are NOT equal
    def test_add_not_equal(self):
        self.assertNotEqual(add(2, 3), 10)

    # assertTrue - passes only if the expression is True
    def test_is_even_true(self):
        self.assertTrue(is_even(4))

    # assertFalse - passes only if the expression is False
    def test_is_even_false(self):
        self.assertFalse(is_even(3))

    # assertIn - checks if a value exists inside a list/string/set
    def test_grade_in_valid_list(self):
        self.assertIn(get_grade(85), ["A", "B", "C", "D", "F"])

    # assertNotIn - checks if a value does NOT exist in a collection
    def test_unknown_grade_not_in(self):
        self.assertNotIn(get_grade(85), ["X", "Y", "Z"])

    # assertIsNotNone - checks the result is not None
    def test_result_is_not_none(self):
        self.assertIsNotNone(add(1, 2))

    # assertRaises - test that the correct exception is raised
    # the test PASSES only if ZeroDivisionError is raised inside the 'with' block
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    # discount > 100 should raise ValueError
    def test_invalid_discount(self):
        with self.assertRaises(ValueError):
            calculate_discount(100, 150)

    # negative discount should also raise ValueError
    def test_negative_discount(self):
        with self.assertRaises(ValueError):
            calculate_discount(100, -10)


# setUp runs automatically BEFORE every single test method in this class
# tearDown runs automatically AFTER every single test method
# use setUp to avoid repeating the same setup code in every test
class TestDiscount(unittest.TestCase):

    def setUp(self):
        # self.price is shared across all test methods in this class
        self.price = 1000

    def tearDown(self):
        # good place for cleanup (close files, db connections, etc.)
        pass

    def test_ten_percent(self):
        self.assertEqual(calculate_discount(self.price, 10), 900)

    def test_twenty_percent(self):
        self.assertEqual(calculate_discount(self.price, 20), 800)

    def test_zero_discount(self):
        # 0% discount means price stays the same
        self.assertEqual(calculate_discount(self.price, 0), 1000)

    def test_full_discount(self):
        # 100% discount means price becomes 0
        self.assertEqual(calculate_discount(self.price, 100), 0)


class TestGrade(unittest.TestCase):

    def test_grade_a(self):
        self.assertEqual(get_grade(95), "A")

    def test_grade_b(self):
        self.assertEqual(get_grade(80), "B")

    def test_grade_c(self):
        self.assertEqual(get_grade(65), "C")

    def test_grade_d(self):
        self.assertEqual(get_grade(45), "D")

    def test_grade_f(self):
        self.assertEqual(get_grade(30), "F")


# allows running this file directly: python 1_unittest_basics.py
if __name__ == "__main__":
    unittest.main()
