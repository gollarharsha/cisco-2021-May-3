import pytest
from phone import Phone


def test_empty_phone(sample_phone):
    assert sample_phone.call_history == []


def test_id_number(sample_phone):
    assert sample_phone.id_number == 1


def test_make_some_calls(sample_phone, good_phone_numbers):
    for one_phone_number in good_phone_numbers:
        assert sample_phone.call(one_phone_number) == 'OK'

    assert sample_phone.call_history == good_phone_numbers


def test_bad_phone_number(sample_phone):
    with pytest.raises(ValueError):
        sample_phone.call('badnum1')
