from greeting import hello


def test_hello():
    output = hello()
    assert output == 'Hello out there!'
