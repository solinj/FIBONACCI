import unittest
import FibonacciGenerator as f
# from mycode import *

class FiboTests(unittest.TestCase):
    def test_5_numb(self):
        self.assertEqual(f.fibo(5), 5)

    def test_6_numb(self):
        self.assertEqual(f.fibo(6), 8)


if __name__ == '__main__':
    unittest.main()













import unittest
import FibonacciGenerator as f

class FiboTest(unittest.TestCase):
    def get_5_number(self):
        self.assertEqual(f.fibo(5), 5)

    def get_6_number(self):
        self.assertEqual(f.fibo(6), 8)

if __name__ == '__main__':
    unittest.main()