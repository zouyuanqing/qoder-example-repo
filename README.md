# Qoder Example Repository

This is an example repository created through Qoder IDE to demonstrate GitHub tool usage.

## Repository Structure

```
.
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   └── example.py
└── tests/
    ├── __init__.py
    └── test_example.py
```

## Files Description

- `README.md` - This file containing project information
- `requirements.txt` - Python package dependencies
- `src/__init__.py` - Makes the src directory a Python package
- `src/example.py` - A simple Python script demonstrating GitHub API usage
- `tests/__init__.py` - Makes the tests directory a Python package
- `tests/test_example.py` - Tests for the example script

## Usage

This repository serves as a demonstration of GitHub API usage through Qoder IDE tools. The example Python script shows how to:

1. Create a function that greets users
2. Handle user input
3. Structure a simple Python project

## Running Tests

To run the tests, execute the following command:

```bash
python -m tests.test_example
```

Or if you're in the project root directory:

```bash
python -m pytest tests/
```

## Example Output

```
Welcome to the Qoder example repository!
What's your name? John
Hello, John! Welcome to the Qoder example repository.
```

## License

This is an example project for demonstration purposes only.