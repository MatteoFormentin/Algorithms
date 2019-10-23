import unittest
from Fuzzy_Match.LevenshteinDistance import *



class TestFuzzyMatch(unittest.TestCase):
    def test_levenshtein_distance(self):
        self.assertEqual(levenshteinDistance("Google", "Facebook"), 8)
        self.assertEqual(levenshteinDistance("Saturday", "Sunday"), 3)
        self.assertEqual(levenshteinDistance("elephant", "relevant"), 3)


if __name__ == '__main__':
    unittest.main()
