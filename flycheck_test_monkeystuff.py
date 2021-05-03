import os


def test_something(monkeypatch):
    monkeypatch.setattr('os.path.join', lambda x: '/etc/passwd')
    

