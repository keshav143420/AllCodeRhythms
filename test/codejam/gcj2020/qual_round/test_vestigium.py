import unittest

import codejam.gcj2020.qual_round.vestigium as vestigium


class VestigiumTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.vestigum = vestigium.Vestigium()

    def test_get_result_sample_data_4d(self):
        n = 4
        arr = [[1, 2, 3, 4],
               [2, 1, 4, 3],
               [3, 4, 1, 2],
               [4, 3, 2, 1]]
        actual_result = self.vestigum.get_result(n, arr)
        expected_result = (4, 0, 0)

        self.assertEqual(expected_result, actual_result)

    def test_get_result_sample_data_3d(self):
        n = 3
        arr = [[2, 1, 3],
               [1, 3, 2],
               [1, 2, 3]]

        actual_result = self.vestigum.get_result(n, arr)
        expected_result = (8, 0, 2)

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
