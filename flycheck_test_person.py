from person import Person

def test_create_person():
    p = Person('first1', 'last1')
    assert isinstance(p, Person)

def test_get_first_name():
    p = Person('first1', 'last1')
    assert p.