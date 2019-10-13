import unittest
from Cryptography.euclidean import *


class TestCrypto(unittest.TestCase):

    def test_euclidean(self):
        a = [0, 1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(euclidean(18, 24), 6)
        self.assertEqual(euclidean(6, 24), 6)


if __name__ == '__main__':
    unittest.main()
