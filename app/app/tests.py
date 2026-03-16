"""
sample tests

"""

from django.test import SimpleTestCase
from app import calc

class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test adding numbers together."""
        res = calc.add(5, 10)

        self.assertEqual(res, 15)
        
    def test_substract_numbers(self):
        """Test subtracting numbers together."""
        res = calc.subtract(10, 15)

        self.assertEqual(res, 5)