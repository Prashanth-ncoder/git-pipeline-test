from calc import average, discount


def test_average():
    assert average([2, 4]) == 3


def test_average_empty_list_returns_zero():
    assert average([]) == 0


def test_average_single_element():
    assert average([10]) == 10


def test_average_single_zero_element():
    assert average([0]) == 0


def test_discount():
    assert discount(100, 10) == 90
