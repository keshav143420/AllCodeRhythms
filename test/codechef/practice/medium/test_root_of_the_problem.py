import unittest

import codechef.practice.medium.root_of_the_problem as root_of_the_problem


class RootOfTheProblemTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.root_of_the_problem = root_of_the_problem.RootOfTheProblem()

    def test_get_the_root_sample_data(self):
        tree = [(4, 0)]
        actual_result = self.root_of_the_problem.get_the_root(tree)
        expected_result = 4
        self.assertEqual(expected_result, actual_result)

        tree = [(1, 5), (2, 0), (3, 0), (4, 0), (5, 5), (6, 5)]
        actual_result = self.root_of_the_problem.get_the_root(tree)
        expected_result = 6
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
