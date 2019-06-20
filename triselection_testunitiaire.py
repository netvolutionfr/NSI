import triselection
import unittest


class TestTriMethods(unittest.TestCase):

    def test_is_sorted(self):
        self.assertTrue(triselection.is_sorted([0, 1, 2, 3, 4, 5, 6]))
        self.assertFalse(triselection.is_sorted([0, 1, 6, 3, 4, 5, 6]))


if __name__ == '__main__':
    unittest.main()