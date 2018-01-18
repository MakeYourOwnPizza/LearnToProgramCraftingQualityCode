import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    def test_num_buses_example_1(self):
        """ Test num_buses when there is no people."""
        actual = a1.num_buses(0)
        expected = 0
        self.assertEqual(expected, actual)
    def test_num_buses_example_2(self):
        """ Test num_buses when there is only one buse, and not full. 1 <= n <=49."""
        actual = a1.num_buses(49)
        expected = 1
        self.assertEqual(expected, actual)
    def test_num_buses_example_3(self):
        """ Test num_buses when there is only one buse, and full. n = 50."""
        actual = a1.num_buses(50)
        expected = 1
        self.assertEqual(expected, actual)
    def test_num_buses_example_4(self):    
        """ Test num_buses when there are more than one bus, but the last one is not full,
        meaning 50 is not a divisor of n."""
        actual = a1.num_buses(99)
        expected = 2
        self.assertEqual(expected, actual)
    def test_num_buses_example_5(self):    

        """Test num_buses when there are more than one bus, and each bus is at
        its full capacity, meaning the number of people is a multiplier of 50."""
        
        actual = a1.num_buses(100)
        expected = 2
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False)
