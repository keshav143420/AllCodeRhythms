import unittest

import hackerearth.algorithms.linear_search.monk_takes_a_walk as mtw


class MonkTakesAWalkTestCase(unittest.TestCase):
    """
    Test cases for hackerearth.practice.linear_search.monk_takes_a_walk solution
    """

    def setUp(self) -> None:
        self.mtw = mtw.MonkTakesAWalk()

    def test_sample_data(self):
        """
        sample test case
        """
        trees = "nBBZLaosnm"
        expected_result = self.mtw.number_of_not_good_trees(trees)
        actual_result = 2
        self.assertEqual(expected_result, actual_result)

    def test_custom_data(self):
        """
        custom test case
        """
        trees = "AEIOUaeiou"
        expected_result = self.mtw.number_of_not_good_trees(trees)
        actual_result = 10
        self.assertEqual(expected_result, actual_result)

        trees = "QWrtY"
        expected_result = self.mtw.number_of_not_good_trees(trees)
        actual_result = 0
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
