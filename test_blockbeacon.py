# test_blockbeacon.py
"""
Tests for BlockBeacon module.
"""

import unittest
from blockbeacon import BlockBeacon

class TestBlockBeacon(unittest.TestCase):
    """Test cases for BlockBeacon class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BlockBeacon()
        self.assertIsInstance(instance, BlockBeacon)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BlockBeacon()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
