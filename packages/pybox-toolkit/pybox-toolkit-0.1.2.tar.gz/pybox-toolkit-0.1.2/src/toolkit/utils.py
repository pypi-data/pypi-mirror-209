"""Miscelaneous utilities for the toolkit"""

class ToolkitException(Exception):
    """Base class for exceptions in the toolkit."""


class RangeException(ToolkitException):
    """Exception raised for invalid range or out-of range variables."""


class ArgumentException(ToolkitException):
    """Exception raised for invalid arguments/missing inputs."""


class DocumentationException(ToolkitException):
    """Exception raised for invalid/missing documentation."""


class TestingException(ToolkitException):
    """Exception raised for invalid/missing/failing tests."""

class RuntimeException(ToolkitException):
    """Exception raised for general runtime errors."""


def ex_assert(condition: bool, exception: Exception):
    """Raise an exception if a condition is not met

    Args:
        condition (bool): Condition to be met
        exception (Exception): Exception to be raised

    Raises:
        exception: If condition is not met
    """
    if not condition:
        raise exception
