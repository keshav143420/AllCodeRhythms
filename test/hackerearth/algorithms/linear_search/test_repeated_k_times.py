import unittest

import hackerearth.algorithms.linear_search.repeated_k_times as rkt


class RepeatedKTimesTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.rkt = rkt.RepeatedKTimes()

    def test_sample_data(self):
        arr = [2, 2, 3, 1, 1]
        k = 2
        actual_result = self.rkt.smallest_k_times_repeated_number(arr, k)
        expected_result = 1
        self.assertEqual(actual_result, expected_result)

    def test_custom_data(self):
        arr = [2, 2, 2, 3, 3, 3, 1, 1]
        k = 3
        actual_result = self.rkt.smallest_k_times_repeated_number(arr, k)
        expected_result = 2
        self.assertEqual(actual_result, expected_result)


if __name__ == '__main__':
    unittest.main()
