from mysum import mysum
import pytest


# def test_mysum_int():
#     assert mysum([10, 20, 30]) == 60


# def test_mysum_float_and_ints():
#     assert mysum([10.2, 20, 30]) == 60.2


# def test_mysum_floats():
#     assert isinstance(mysum([1.2, 3.4]), float)


@pytest.mark.parametrize('numbers, result',    # what parameter values are we passing?
                         [
                             # list of tuples, each tuple with param values
                             ([10, 20, 30], 60),
                             ([10.2, 20, 30], 60.2),
                             ([1.2, 3.4], 4.6)
                         ])
def test_mysum(numbers, result):
    assert mysum(numbers) == result


def test_mysum_strings():
    with pytest.raises(TypeError):
        # secret __enter__ method
        assert mysum(['a', 'b', 'c'])
        # secret __exit__ method
