from add_numbers import add_numbers
from io import StringIO
import pytest

@pytest.fixture
def fake_input():
    return StringIO('10 20')

def test_simple_adding(monkeypatch, fake_input):
    monkeypatch.setattr('sys.stdin', fake_input(