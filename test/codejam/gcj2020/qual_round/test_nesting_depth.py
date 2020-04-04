import unittest

from codejam.gcj2020.qual_round import nesting_depth


class NestingDepthTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.nesting_depth = nesting_depth.NestingDepth()

    def test_get_nesting_depth_sample_data(self):
        num_str = "1234"
        actual_result = self.nesting_depth.get_nesting_depth(num_str)
        expected_result = "(1(2(3(4))))"
        self.assertEqual(expected_result, actual_result)

    def test_get_nesting_depth_custom_data(self):
        num_str = "0213124221"
        actual_result = self.nesting_depth.get_nesting_depth(num_str)
        expected_result = "0((2)1((3))1(2((4))22)1)"
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
