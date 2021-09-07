import unittest
from src.calculator import add, divide, multiply, subtract

class TestCalculator(unittest.TestCase):
    pass

    def test_add(self):
        self.assertEqual(5, add(2,3))

    # def test_add(self):
        # expected = 5
        # actual = add(2, 3)
        # self.assertEqual(expected, actual)

    def test_subtract(self):
        self.assertEqual(3, subtract(10,7))

    def test_divide(self):
        self.assertEqual(2, divide(4, 2))

    def test_multiply(self):
        self.assertEqual(36, multiply(6, 6))