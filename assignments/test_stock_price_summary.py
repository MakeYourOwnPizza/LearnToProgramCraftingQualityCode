import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    def test_stock_price_summary_empty_list(self):
        """Test stock_price_summary when the list is empty."""

        actual = a1.stock_price_summary([])
        expected = (0, 0)
        self.assertEqual(expected, actual)
        
    def test_stock_price_summary_example_1(self):
        """Test stock_price_summary when there are only zeros."""

        actual = a1.stock_price_summary([0, 0])
        expected = (0, 0)
        self.assertEqual(expected, actual)
        
    def test_stock_price_summary_example_2(self):
        """Test stock_price_summary when there are only gains."""

        actual = a1.stock_price_summary([0.01, 0.03, 0.10])
        expected = (0.14, 0)
        self.assertEqual(expected, actual)
        
    def test_stock_price_summary_example_3(self):
        """Test stock_price_summary when there are only losses."""

        actual = a1.stock_price_summary([-0.02, -0.14, -0.01])
        expected = (0, -0.17)
        self.assertEqual(expected, actual)
        
    def test_stock_price_summary_example_4(self):
        """Test stock_price_summary when there are gains and losses."""

        actual = a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0.10, -0.01])
        expected = (0.14, -0.17)
        self.assertEqual(expected, actual)
        
    def test_stock_price_summary_example_5(self):
        """Test stock_price_summary when the there are only gains and zeros"""

        actual = a1.stock_price_summary([0.01, 0.03, 0, 0, 0.10])
        expected = (0.14, 0)
        self.assertEqual(expected, actual)
        
    def test_stock_price_summary_example_6(self):
        """Test stock_price_summary when there are only losses and zeros."""

        actual = a1.stock_price_summary([-0.02, -0.14, 0, 0, -0.01])
        expected = (0, -0.17)
        self.assertEqual(expected, actual)
        
    def test_stock_price_summary_example_7(self):
        """Test stock_price_summary when there are gains, losses, and zeros."""

        actual = a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
        expected = (0.14, -0.17)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(exit=False)
