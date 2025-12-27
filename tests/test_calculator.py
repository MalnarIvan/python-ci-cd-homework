import sys
import os
import time
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from calculator import factorial


class TestCalculator(unittest.TestCase):

    def test_factorial_of_zero(self):
        time.sleep(0.5)  # искусственная задержка
        self.assertEqual(factorial(0), 1)

    def test_factorial_of_positive_number(self):
        time.sleep(0.5)  # искусственная задержка
        self.assertEqual(factorial(5), 120)

    def test_factorial_negative_number(self):
        time.sleep(0.5)  # искусственная задержка
        with self.assertRaises(ValueError):
            factorial(-1)


if __name__ == "__main__":
    unittest.main()
