import os


def test_something(monkeypatch):
    # replace the os.path.join function with a lambda!
    monkeypatch.setattr('os.path.join', lambda x: '/etc/passwd')
    print(os.path.join('stuff'))
