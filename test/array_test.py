import unittest
from Arrays.BinarySearch import *
from Arrays.Mergesort import *


class TestArray(unittest.TestCase):

    def test_binary_search(self):
        a = [0, 1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(binarySearch(a, 2, 0, len(a)-1), 2)
        self.assertEqual(binarySearch(a, 7, 0, len(a)-1), 7)
        self.assertEqual(binarySearch(a, 3, 0, len(a)-1), 3)

    def test_merge_sort(self):
        self.assertEqual(mergeSort([1, 3, 5, 2, 7, 4, 9, 0, 23]), [
                         0, 1, 2, 3, 4, 5, 7, 9, 23])
        self.assertEqual(mergeSort([12, 15, 23, 4, 6, 10, 35]), [
                         4, 6, 10, 12, 15, 23, 35])


if __name__ == '__main__':
    unittest.main()
