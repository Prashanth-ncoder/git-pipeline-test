from calc import average, discount


def test_average():
    assert average([2, 4]) == 3


def test_average_empty_list_returns_zero():
    assert average([]) == 0


def test_average_single_element():
    assert average([10]) == 10


def test_average_single_zero_element():
    assert average([0]) == 0


def test_average_volume_large_list():
    values = list(range(100_000))
    assert average(values) == 49999.5


def test_average_non_numeric_still_raises_type_error():
    # Non-numeric input is out of scope for QT-14; it keeps its current behaviour.
    import pytest

    with pytest.raises(TypeError):
        average(["a", "b"])


def test_discount():
    assert discount(100, 10) == 90
