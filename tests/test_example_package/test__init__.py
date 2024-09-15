"""Testcases for example_module.py go here."""

import unittest
from unittest.mock import patch
from io import StringIO
from src.main import entry_point
from src.example_package.example_module import my_sum


class TestEntryPoint(unittest.TestCase):
    @patch("sys.stdout", new_callable=StringIO)  # Mock stdout to capture prints
    @patch("sys.argv", ["entry_point", "2", "3"])  # Mock command-line arguments
    def test_entry_point(self, mock_stdout):
        # Call the entry point
        entry_point()

        # Check if the output is correct
        output = mock_stdout.getvalue().strip()  # Capture printed output
        self.assertEqual(output, "5.0")  # Expecting the sum of 2 and 3 (5.0)

    def test_my_sum(self):
        # Example test for the my_sum function directly
        self.assertEqual(my_sum(2, 3), 5.0)
        self.assertEqual(my_sum(10.5, 4.5), 15.0)


if __name__ == "__main__":
    unittest.main()
