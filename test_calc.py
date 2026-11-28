from calc import average, discount


def test_average():
    assert average([2, 4]) == 3


def test_discount():
    assert discount(100, 10) == 90
