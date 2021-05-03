from greeting import hello


def test_hello(capsys):
    hello()
    captured_out, captured_err = capsys.readouterr()
    assert captured_out == 'Hello out there!'
