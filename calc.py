"""Small helper module for the non-Salesforce review test."""


def average(values):
    """Return the mean of a list of numbers."""
    return sum(values) / len(values)


def discount(price, percent):
    """Return the price after a percent discount."""
    return price - price * percent / 100
