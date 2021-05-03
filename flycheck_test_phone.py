import pytest
from phone import Phone


@pytest.fixture
def sample_phone():
    return Phone(1)


@pytest.fixture
def good_phone_numbers():
    return ['12345', '67890', '2468', '1357']

def test_empty_phone(sample_phone):
    assert sample_phone.call_history == []


def test_id_number(sample_phone):
    assert sample_phone.id_number == 1


def test_make_some_calls(sample_phone, good_phone_numbers):
    for one_phone_number in good_phone_numbers:
        
    sample_phone.call('12345')
    sample_phone.call('67890')
    assert '12345' in sample_phone.call_history
    assert '67890' in sample_phone.call_history


def test_bad_phone_number(sample_phone):
    with pytest.raises(ValueError):
        sample_phone.call('badnum1')
