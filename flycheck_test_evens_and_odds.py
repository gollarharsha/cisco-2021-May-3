from evens_and_odds import evens_and_odds

def test_no_numbers():
    output = evens_and_odds([])
    assert output['evens'