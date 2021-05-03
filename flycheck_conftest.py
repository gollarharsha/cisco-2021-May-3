check @pytest.fixture(scope='session')
def a_person():
    p = Person('first1', 'last1')
    return p

