from person import Person
import pytest

@pytest.fixture
def a_person():
    p = Person('first1', 'last1')
    return p


def test_create_person(a_person):
    assert isinstance(p, Person)


def test_get_first_name():
    p = Person('first1', 'last1')
    assert p.first_name == 'first1'


def test_get_last_name():
    p = Person('first1', 'last1')
    assert p.last_name == 'last1'
