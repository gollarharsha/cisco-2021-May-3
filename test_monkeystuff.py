from monkeystuff import say_hello
from io import StringIO
import os
importt pytest


# def test_something(monkeypatch):
#     # replace the os.path.join function with a lambda!
#     monkeypatch.setattr('os.path.join', lambda x: '/etc/passwd')
#     print(os.path.join('stuff'))

@pytest.fixture
def fake_name_input():
    s = StringIO('Reuven\n')


def test_say_hello():
    output = say_hello()
    assert output == 'Hello, Reuven!'
