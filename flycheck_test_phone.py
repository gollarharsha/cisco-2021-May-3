import pytest
from phone import Phone

@pytest.fixture
def sample_phone():
    return Phone(1)


def test_empty_phone(sample_phone):
    assert sample_phone.call_history == []


def test_id_number():
    p = Phone(1)
    assert p.id_number == 1


def test_make_some_calls():
    p = Phone(1)
    p.call('12345')
    p.call('67890')
    assert '12345' in p.call_history
    assert '67890' in p.call_history


def test_bad_phone_number():
    p = Phone(1)
    with pytest.raises(ValueError):
        p.call('badnum1')
