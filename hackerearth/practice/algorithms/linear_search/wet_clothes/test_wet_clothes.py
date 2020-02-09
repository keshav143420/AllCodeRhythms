import unittest

from hackerearth.practice.algorithms.linear_search.wet_clothes.wet_clothes import WetClothes


class WetClothesTestCase(unittest.TestCase):

    def test_sample_data(self):
        (n, m, g) = (3, 3, 2)
        n_array = [3, 5, 8]
        a_array = [4, 1, 3]
        wc = WetClothes()
        actual_result = wc.saved_wet_cloths(n, m, g, n_array, a_array)
        expected_result = 2

        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
