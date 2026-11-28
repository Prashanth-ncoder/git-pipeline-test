"""Simple inventory helpers."""


def add_item(stock, item, qty=1):
    """Add qty of item to the stock dict and return it."""
    stock[item] = stock.get(item, 0) + qty
    return stock


def remove_item(stock, item, qty=1):
    """Remove qty of item; never goes below zero."""
    if item in stock:
        stock[item] = max(0, stock[item] - qty)
    return stock
