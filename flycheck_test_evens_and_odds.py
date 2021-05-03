from evens_and_odds import evens_and_odds


def test_returns_a_dict():

    output = evens_and_odds([10, 11, 12])
    assert isinstance(output, dict)


def test_no_numbers():
    output = evens_and_odds([])
    assert output['evens'] == []
    assert output['odds'] == []


def test_only_evens():
    output = evens_and_odds([6, 8, 10])
    assert output['evens'] == [6, 8, 10]
    assert output['odds'] == []


def test_only_odds():
    output = evens_and_odds([5, 3, 7])
    assert output['evens'] == []
    assert output['odds'] == [5, 3, 7]
