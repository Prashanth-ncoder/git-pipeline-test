from app.greeting import greet, shout
from app.inventory import add_item, remove_item


def test_greet():
    assert greet("Ann") == "Hello, Ann!"


def test_shout():
    assert shout("Ann") == "HELLO, ANN!"


def test_add_and_remove():
    stock = add_item({}, "pen", 2)
    assert remove_item(stock, "pen", 5)["pen"] == 0
