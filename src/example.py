#!/usr/bin/env python3
"""
Example Python script created through Qoder IDE
Demonstrates basic GitHub API usage
"""

def greet(name):
    """Return a greeting message"""
    return f"Hello, {name}! Welcome to the Qoder example repository."

def main():
    """Main function"""
    print("Welcome to the Qoder example repository!")
    name = input("What's your name? ")
    print(greet(name))

if __name__ == "__main__":
    main()