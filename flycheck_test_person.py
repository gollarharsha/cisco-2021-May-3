from person import Person


def test_create_person():
    p = Person('first1', 'last1')
    assert isinstance(p, Person)


def test_get_first_name():
    p = Person('first1', 'last1')
    assert p.first_name == 'first1'


def test_get_last_name():
    p = Person('first1', 'last1')
    assert p.last_name == 'last1'
