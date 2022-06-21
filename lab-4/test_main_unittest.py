import unittest
from main import add, sub, root, factorial


class TestFactorial(unittest.TestCase):
    def test_expected_values(self):
        self.assertAlmostEqual(factorial(1), 1)
        self.assertAlmostEqual(factorial(0), 1)

    def test_wrong_values(self):
        self.assertRaises(ValueError, factorial, -2)

    def test_wrong_types(self):
        self.assertRaises(TypeError, factorial, True)
        self.assertRaises(TypeError, factorial, 3 + 8j)
        self.assertRaises(TypeError, factorial, "kolo")


class TestAddition(unittest.TestCase):
    def test_expected_values(self):
        self.assertAlmostEqual(add(1, 1), 2)
        self.assertAlmostEqual(add(-2, 2), 0)

    def test_wrong_types(self):
        self.assertRaises(TypeError, add, "kolo", 2)
        self.assertRaises(TypeError, add, True, False)

    # def test_wrong_values(self):
    #     self.assertRaises(ValueError, add, 2, 0)


class TestSubtraction(unittest.TestCase):
    def test_expected_values(self):
        self.assertAlmostEqual(sub(2, 2), 0)

    def test_wrong_types(self):
        self.assertRaises(TypeError, sub, "kolo", 2)
        self.assertRaises(TypeError, sub, True, False)

    # def test_wrong_values(self):
    #     self.assertRaises(ValueError, sub, 2, -0.1)


class TestRoot(unittest.TestCase):
    def test_expected_values(self):
        self.assertAlmostEqual(root(27, 3), 3)

    def test_wrong_types(self):
        self.assertRaises(TypeError, root, 2, "root")
        self.assertRaises(TypeError, root, 'H', 3)
        self.assertRaises(TypeError, root, 2.5, 3)

    def test_wrong_values(self):
        self.assertRaises(ValueError, root, -2, 2)


if __name__ == "__main__":
    unittest.main()
