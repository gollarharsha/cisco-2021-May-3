from mysum 

def test_mysum_int():
    assert mysum([10, 20, 30]) == 60


def test_mysum_float_and_ints():
    assert mysum([10.2, 20, 30]) == 60.2
