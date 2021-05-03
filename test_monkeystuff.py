import os


def test_something(monkeypatch):
    monkeypatch.setattr('os.pathsep', '||')
    print(os.pathsep)
    # print(os.path.join('abcd', 'efgh', 'ijkl'))
