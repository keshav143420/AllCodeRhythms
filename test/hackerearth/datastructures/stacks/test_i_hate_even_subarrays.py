import unittest

import hackerearth.datastructures.stacks.i_hate_even_subarrays as ihes


class IHateEvenSubArraysTestCase(unittest.TestCase):
    """
    Test cases for hackerearth.practice.linear_search.wet_clothes solution
    """

    def setUp(self) -> None:
        self.ihes = ihes.IHateEvenSubArrays()

    def test_minimize_size_by_removing_even_sub_arrays(self):
        """
        sample test case
        """
        wc = ihes.IHateEvenSubArrays()
        actual_result = wc.minimize_size_by_removing_even_sub_arrays("101001")
        expected_result = "10"
        self.assertEqual(expected_result, actual_result)

    def test_minimize_size_by_removing_even_sub_arrays_empty_array(self):
        wc = ihes.IHateEvenSubArrays()
        actual_result = wc.minimize_size_by_removing_even_sub_arrays("0000")
        expected_result = "KHALI"
        self.assertEqual(expected_result, actual_result)

    def test_minimize_size_by_removing_even_sub_arrays_odd_length(self):
        wc = ihes.IHateEvenSubArrays()
        actual_result = wc.minimize_size_by_removing_even_sub_arrays("111")
        expected_result = "1"
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
