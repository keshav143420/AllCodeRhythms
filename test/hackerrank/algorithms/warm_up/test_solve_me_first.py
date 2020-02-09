import math
import random
import unittest

from hackerrank.algorithms.warm_up.solve_me_first import SolveMeFirst


class TestSolveMeFirst(unittest.TestCase):
    def test_solve_me_first_sample_data(self):
        num1 = 10
        num2 = 20
        smf = SolveMeFirst(num1, num2)
        expected_result = 30
        actual_result = smf.solve_me_first()
        self.assertEqual(expected_result, actual_result)

    def test_solve_me_first_random_data(self):
        num1 = math.floor(random.random() * 200 // 2)
        num2 = math.floor(random.random() * 200 // 2)
        smf = SolveMeFirst(num1, num2)
        expected_result = num1 + num2
        actual_result = smf.solve_me_first()
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
