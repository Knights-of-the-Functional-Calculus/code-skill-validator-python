import unittest

import factorial

class TestFactorial(unittest.TestCase):
    def test_base_case(self):
        self.assertEqual(factorial(0), 1)

    def test_other(self):
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(8),  40320)

if __name__ == '__main__':
	unittest.main()