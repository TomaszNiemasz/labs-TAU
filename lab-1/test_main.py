import unittest
from main import calc_area_of_circle, calc_factorial, compare_numbers
from math import pi


class TestAreaOfCircle(unittest.TestCase):
    def test_expected_values(self):
        self.assertAlmostEqual(calc_area_of_circle(1), pi)
        self.assertAlmostEqual(calc_area_of_circle(0), 0)

    def test_wrong_values(self):
        # must raise value error
        self.assertRaises(ValueError, calc_area_of_circle, -3)

    def test_type(self):
        # must not raise type error
        self.assertRaises(TypeError, calc_area_of_circle, 4)

    def test_wrong_types(self):
        # must raise type error
        self.assertRaises(TypeError, calc_area_of_circle, "circle")
        self.assertRaises(TypeError, calc_area_of_circle, True)
        self.assertRaises(TypeError, calc_area_of_circle, 4j + 7)


class TestFactorial(unittest.TestCase):
    def test_expected_values(self):
        self.assertAlmostEqual(calc_factorial(0), 1)
        self.assertAlmostEqual(calc_factorial(1), True)

    def test_wrong_values(self):
        # must raise value error
        self.assertRaises(ValueError, calc_factorial, -2)

    def test_type(self):
        # must not raise type error
        self.assertRaises(TypeError, calc_factorial, 5)

    def test_wrong_types(self):
        # must raise type error
        self.assertRaises(TypeError, calc_factorial, "factorial")
        self.assertRaises(TypeError, calc_factorial, True)
        self.assertRaises(TypeError, calc_factorial, 4j + 7)


class TestComparison(unittest.TestCase):
    def test_expected_values(self):
        self.assertEquals(compare_numbers(2, 4), False)
        self.assertEquals(compare_numbers(2, 2), True)
        self.assertEquals(compare_numbers(-3, -3), True)

    def test_type(self):
        # must not raise type error
        self.assertRaises(TypeError, compare_numbers, 3, 6)

    def test_wrong_types(self):
        self.assertRaises(TypeError, compare_numbers, 5, True)
        self.assertRaises(TypeError, compare_numbers, 7 + 4j, None)
        self.assertRaises(TypeError, compare_numbers, "number", 3)
