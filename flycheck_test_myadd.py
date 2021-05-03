from myadd import add


def test_add_positive_ints():
    print('Checking positive ints')
    assert add(2, 2) == 4


def test_add_negative_ints():

    assert add(-2, -2) == -4


def test_add_mixed_ints():
    assert add(2, -2) == 0


def test_add_strings():
    assert add('abcd', 'efgh') == 'abcdefgh'
