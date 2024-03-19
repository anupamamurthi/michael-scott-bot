
import unittest

from michael_scott_bot.constants import VERSION


class TestRunInitial(unittest.TestCase):
    """Test the Constants.
    Basic Test class to verify repo is setup correctly.
    """

    def test_version(self):
        """Test version is set works"""
        self.assertIsNotNone(VERSION)
        self.assertEqual(VERSION, "0.0.1")
