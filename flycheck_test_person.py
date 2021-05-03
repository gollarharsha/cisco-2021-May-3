from person import Person
import pytest




def test_create_person(a_person):
    assert isinstance(a_person, Person)


def test_get_first_name(a_person):
    assert a_person.first == 'first1'


def test_get_last_name(a_person):
    assert a_person.last == 'last1'


def test_fullname(a_person):
    assert a_person.fullname() == 'first1 last1'


def test_greet(a_person):
    assert a_person.greet() == 'Hello, first1 last1'
