import unittest

from codechef.practice.easy.nuclear_reactors import NuclearReactor


class TestNuclearReactor(unittest.TestCase):

    def test_get_final_state_sample_data(self):
        (a, n, k) = (3, 1, 3)
        expected_result = "1 1 0"
        nr = NuclearReactor(a, n, k)
        result = nr.get_final_state()
        actual_result = " ".join([str(i) for i in result])
        self.assertEqual(expected_result, actual_result)

    def test_get_final_state_one_atom(self):
        (a, n, k) = (1, 1, 3)
        expected_result = "1 0 0"
        nr = NuclearReactor(a, n, k)
        result = nr.get_final_state()
        actual_result = " ".join([str(i) for i in result])
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()
