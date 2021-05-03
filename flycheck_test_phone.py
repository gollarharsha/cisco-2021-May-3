from phone import Phone


def test_empty_phone():
    p = Phone()
    assert p.call_history == []

def test_make_some_calls():
    p = Phone()
    p.call('12345')
    p.call('67890')
    assert '12345' in p.call_history
    assert '67890