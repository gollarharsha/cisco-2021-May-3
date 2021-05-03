from person import Person
import pytest


@pytest.fixture
def a_person():
    p = Person('first1', 'last1')
    return p


def test_create_person(a_person):
    assert isinstance(a_person, Person)


def test_get_first_name(a_person):
    assert a_person.first_name == 'first1'


def test_get_last_name(a_person):
    p = Person('first1', 'last1')
    assert p.last_name == 'last1'
