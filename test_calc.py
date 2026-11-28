from calc import average, discount


def test_average():
    assert average([2, 4]) == 3


def test_average_empty_list_returns_zero():
    assert average([]) == 0


def test_discount():
    assert discount(100, 10) == 90
