def mysum(numbers):
    total = 0

    for one_number in numbers:
        total += one_number

    return total


def test_mysum_int():
    assert mysum([10, 20, 30]) == 60


    assert mysum([10.2, 20, 30]) == 60.2
