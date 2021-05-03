from person import Person

def test_create_person():
    p = Person('first1', 'last1')
    assert isinstance(p, Person)