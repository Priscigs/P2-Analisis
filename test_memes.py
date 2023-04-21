import unittest
from memes import lcs_dynamic as lcs_dynamic
from memes import lcs_divide_conquer as lcs_divide


class TestLcsDynamic(unittest.TestCase):
    def test_lcs_dynamic_basic_input(self):
        self.assertEqual(lcs_dynamic("abcde", "ace"), "ACE")

    def test_lcs_dynamic_case_sensitivity(self):
        self.assertEqual(lcs_dynamic("AbCdEfG", "aCeG"), "ACEG")

    def test_lcs_dynamic_empty_input(self):
        self.assertEqual(lcs_dynamic("", "abc"), "")
        self.assertEqual(lcs_dynamic("abc", ""), "")
        self.assertEqual(lcs_dynamic("", ""), "")

    def test_lcs_dynamic_same_input(self):
        self.assertEqual(lcs_dynamic("abc", "abc"), "ABC")

    def test_lcs_dynamic_no_common_subsequence(self):
        self.assertEqual(lcs_dynamic("abcde", "fghij"), "")

    def test_lcs_dynamic_mapola(self):
        self.assertEqual(lcs_dynamic("matamoscas", "amapolas"), "AMOAS")

class TestLcsDivideAndConquer(unittest.TestCase):
    def test_lcs_divide_basic_input(self):
        self.assertEqual(lcs_divide("abcde", "ace"), "ACE")

    def test_lcs_divide_case_sensitivity(self):
        self.assertEqual(lcs_divide("AbCdEfG", "aCeG"), "ACEG")

    def test_lcs_divide_empty_input(self):
        self.assertEqual(lcs_divide("", "abc"), "")
        self.assertEqual(lcs_divide("abc", ""), "")
        self.assertEqual(lcs_divide("", ""), "")

    def test_lcs_divide_same_input(self):
        self.assertEqual(lcs_divide("abc", "abc"), "ABC")

    def test_lcs_divide_no_common_subsequence(self):
        self.assertEqual(lcs_divide("abcde", "fghij"), "")

    def test_lcs_divide_mapola(self):
        self.assertEqual(lcs_divide("amapolas", "matamoscas"), "AMOAS")

if __name__ == '__main__':
    unittest.main()
