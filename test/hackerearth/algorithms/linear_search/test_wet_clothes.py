import unittest

import hackerearth.algorithms.linear_search.wet_clothes as wcm


class WetClothesTestCase(unittest.TestCase):
    """
    Test cases for hackerearth.practice.linear_search.wet_clothes solution
    """

    def setUp(self) -> None:
        self.wcp = wcm.WetClothesP()

    def test_sample_data(self):
        """
        sample test case
        """

        (self.wcp.no_completely_wet_clothes,
         self.wcp.no_time_intervals,
         self.wcp.limit_to_dry) = (3, 3, 2)
        self.wcp.time_intervals = [3, 5, 8]
        self.wcp.dry_rate = [4, 1, 3]
        wc = wcm.WetClothes()
        actual_result = wc.saved_wet_cloths(self.wcp)
        expected_result = 2

        self.assertEqual(expected_result, actual_result)

    def test_sample_custom_data(self):
        """
        sample test case
        """
        (self.wcp.no_completely_wet_clothes,
         self.wcp.no_time_intervals,
         self.wcp.limit_to_dry) = (3, 3, 2)
        self.wcp.time_intervals = [3, 5, 6]
        self.wcp.dry_rate = [4, 1, 3]
        wc = wcm.WetClothes()
        actual_result = wc.saved_wet_cloths(self.wcp)
        expected_result = 1

        self.assertEqual(expected_result, actual_result)

    def test_sample_custom_large_data(self):
        """
        sample test case
        """
        (self.wcp.no_completely_wet_clothes,
         self.wcp.no_time_intervals,
         self.wcp.limit_to_dry) = (2, 100, 5)
        self.wcp.time_intervals = [861, 3048]
        self.wcp.dry_rate = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
                             1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        wc = wcm.WetClothes()
        actual_result = wc.saved_wet_cloths(self.wcp)
        expected_result = 100

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
