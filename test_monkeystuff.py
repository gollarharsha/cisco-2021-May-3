import os


def test_something(monkeypatch):
    monkeypatch('os.pathsep', '||')
    print(os.path.join('abcd', 'efgh', 'ijkl'))
