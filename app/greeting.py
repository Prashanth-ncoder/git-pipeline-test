"""Greeting helpers."""


def greet(name):
    """Return a greeting for the given name."""
    return f"Hello, {name}!"


def shout(name):
    """Return the greeting in upper case."""
    return greet(name).upper()
