from phone import Phone
from person import Person
import pytest


@pytest.fixture(scope='session')
def a_person():
    p = Person('first1', 'last1')
    return p


@pytest.fixture
def sample_phone(autouse=True):
    return Phone(1)


@pytest.fixture
def good_phone_numbers():
    return ['12345', '67890', '2468', '1357']
