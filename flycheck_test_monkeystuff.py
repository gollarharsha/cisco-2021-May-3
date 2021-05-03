from monkeystuff import say_hello

import os


# def test_something(monkeypatch):
#     # replace the os.path.join function with a lambda!
#     monkeypatch.setattr('os.path.join', lambda x: '/etc/passwd')
#     print(os.path.join('stuff'))

def test_say_hello():
    output = say_hello()
    assert output == 'Hello, Reuven!'
