def add(first, second):
    return first + second


def test_add_positive_ints():
    assert add(2, 2) == 4


def test_add_negative_ints():
    assert add(-2, -2) == -4


def test_add_mixed_ints():
    assert add(2, -2) == 0


def test_add_strings():
    assert add('abcd', 'efgh') == 'abcdefgh'
