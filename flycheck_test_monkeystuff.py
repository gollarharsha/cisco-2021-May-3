import os


def test_something(monkeypatch):
    monkeypatch.setattr('os.path.join', '/etc/passwd')
    print(os.path
