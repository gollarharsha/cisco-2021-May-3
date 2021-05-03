from phone import Phone


def test_empty_phone():
    p = Phone()
    assert p.call_history == []

def test_make_some_calls():
    