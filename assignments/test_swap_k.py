import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    def test_testswap_k_example_1(self):
        """Test the case when k == 0, thus L keeps the same, no matter how long L is."""
        nums = [1,2,3,4,5,6]
        a1.swap_k(nums, 0)
        actual = nums
        expected = [1,2,3,4,5,6]
        self.assertEqual(expected,actual)
        

    def test_testswap_k_example_2(self):
        """Test the case when k == 1."""
        nums = [1,2]
        a1.swap_k(nums,1)
        actual = nums
        expected = [2,1]
        self.assertEqual(expected,actual)

    def test_testswap_k_example_3(self):
        """Test the case when k > 1."""
        nums = [1,2,3,4,5]
        a1.swap_k(nums,2)
        actual = nums
        expected = [4,5,3,1,2]
        self.assertEqual(expected,actual)

if __name__ == '__main__':
    unittest.main(exit=False)
