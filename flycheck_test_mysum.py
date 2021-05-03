from mysum import mysum
import pytest


# def test_mysum_int():
#     assert mysum([10, 20, 30]) == 60


# def test_mysum_float_and_ints():
#     assert mysum([10.2, 20, 30]) == 60.2


# def test_mysum_floats():
#     assert isinstance(mysum([1.2, 3.4]), float)


@pytest.mark.parameterize('numbers


def test_mysum_strings():
    with pytest.raises(TypeError):
        # secret __enter__ method
        assert mysum(['a', 'b', 'c'])
        # secret __exit__ method
