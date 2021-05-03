from person import Person
import pytest


# decorator -- only affects the one function coming after it
# @pytest.fixture(scope='session')
# def a_person():
#     p = Person('first1', 'last1')
#     return p

@pytest.fixture(params=[('first1', 'last1'),
                        ('first2', 'last2')],
                scope='session')
def a_person(request):
    p = Person(request.param[0],
               request.param[1])
    return p




@pytest.fixture
def five():
    
    yield 5   # everything before the "yield" is setup / everything after is teardown


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
