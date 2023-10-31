# Test-driven Development in Python

## What's an Interactive Test

Interactive testing, often known as exploratory testing, is a manual approach to testing software. Testers interact with the application in real-time to discover issues, evaluate usability, and ensure that the software behaves as expected. It involves running the software and trying different inputs or actions to uncover unexpected behavior.

## Why Tests are Important

Testing is crucial for software development for several reasons:

- **Bug Identification:** Tests help identify and fix bugs early in the development process, reducing the likelihood of issues in production.
- **Regression Prevention:** Tests ensure that new code changes don't break existing functionality (regressions).
- **Documentation:** Tests serve as documentation, providing usage examples for other developers.
- **Improved Code Quality:** Writing tests often leads to better-structured and modular code.
- **Confidence:** Tests provide confidence that the software functions as intended.

## How to Write Docstrings to Create Tests

In Python, you can use docstrings to create tests using libraries like doctest or Sphinx. To write tests within docstrings, use examples that demonstrate how a function or method should behave. Here's an example using doctest:

```python
def add(a, b):
    """
    This function adds two numbers.

    >>> add(2, 3)
    5
    >>> add(0, 0)
    0
    """
    return a + b
```

## How to Write Documentation for Each Module and Function

Documentation is essential for code maintainability. You can write docstrings for modules, functions, and classes. Here's how to write module-level and function-level docstrings:

```python
# Module-level docstring
"""
This module contains utility functions for math operations.
"""

# Function-level docstring
def add(a, b):
    """
    Adds two numbers.

    :param a: The first number.
    :param b: The second number.
    :return: The sum of a and b.
    """
    return a + b
```

## Basic Option Flags to Create Tests

In Python, popular testing frameworks like `unittest`, `pytest`, and `nose` allow you to use various option flags to control test execution. Some common options include:

- `-v` or `--verbose`: Increase verbosity to see more detailed test output.
- `-k` or `--keyword`: Run tests that match a specified keyword.
- `-x` or `--exitfirst`: Stop test execution after the first failure.
- `-s` or `--nocapture`: Disable stdout/stderr capturing.
- `-m` or `--markers`: Select tests based on markers.
- `-n` or `--numprocesses`: Parallelize test execution by specifying the number of processes.

Each testing framework may have its own set of option flags.

## How to Find Edge Cases

Finding edge cases is essential for thorough testing. To find edge cases, consider the following strategies:

- **Boundary Values:** Test at the boundaries of input ranges (minimum and maximum values).
- **Empty Inputs:** Test with empty strings, lists, or other data structures.
- **Null Values:** Test with `None` or null values.
- **Exception Cases:** Test with inputs that should raise exceptions.
- **Overflows:** Test with inputs that might cause numeric overflows or other errors.
- **Corner Cases:** Consider unique or rare scenarios that could result in unexpected behavior.

The goal is to explore scenarios that might not be immediately obvious and ensure the software can handle them effectively.

Remember that comprehensive testing involves both normal use cases and edge cases to ensure software reliability and robustness.
