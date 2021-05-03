from monkeystuff import say_hello
from io import StringIO
import os
import pytest


# def test_something(monkeypatch):
#     # replace the os.path.join function with a lambda!
#     monkeypatch.setattr('os.path.join', lambda x: '/etc/passwd')
#     print(os.path.join('stuff'))

@pytest.fixture
def fake_name_input():
    return StringIO('Reuven\n')


def test_say_hello(monkeypatch, fake_name_input):
    monkeypatch.setattr('sys.stdin', fake_name_input)
    output = say_hello()
    assert output == 'Hello, Reuven!'
