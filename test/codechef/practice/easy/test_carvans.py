from unittest import TestCase

from codechef.practice.easy.carvans import CarVans


class TestCarVans(TestCase):
    def test_moving_maximum_speed(self):
        arr = [4, 5, 1, 2, 3]
        cv = CarVans()
        actual_result = cv.maximum_speed(arr)
        expected_result = 2
        self.assertEqual(actual_result, expected_result)
