#!/usr/bin/env python3
"""
Test file for example.py script
"""

import sys
import os

# Add the src directory to the path so we can import the example module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from example import greet

def test_greet():
    """Test the greet function"""
    # Test with a normal name
    result = greet("Alice")
    expected = "Hello, Alice! Welcome to the Qoder example repository."
    assert result == expected, f"Expected '{expected}', but got '{result}'"
    
    # Test with an empty string
    result = greet("")
    expected = "Hello, ! Welcome to the Qoder example repository."
    assert result == expected, f"Expected '{expected}', but got '{result}'"
    
    print("All tests passed!")

if __name__ == "__main__":
    test_greet()