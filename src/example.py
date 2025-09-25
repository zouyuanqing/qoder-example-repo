#!/usr/bin/env python3
"""
Example Python script created through Qoder IDE
Demonstrates basic GitHub API usage
"""

import sys
import argparse

def greet(name):
    """Return a greeting message"""
    return f"Hello, {name}! Welcome to the Qoder example repository."

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="Qoder Example Script")
    parser.add_argument("--name", "-n", help="Your name")
    args = parser.parse_args()
    
    if args.name:
        name = args.name
    else:
        name = input("What's your name? ")
    
    print(greet(name))

if __name__ == "__main__":
    main()