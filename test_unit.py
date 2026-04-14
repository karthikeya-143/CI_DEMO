import unittest
from example import add, mul

class TestExample(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-1, 1), 0)


    def test_mul(self):
        self.assertEqual(mul(5, 3), 15)
        self.assertEqual(mul(-1, 1), -1)

if __name__ == '__main__':
    unittest.main()