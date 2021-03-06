import pytest
from file_length import file_length


@pytest.fixture
def short_file(tmp_path):
    with open(tmp_path / 'short_file.txt', 'w') as f:
        f.write('abcd\n')
        f.write('efgh\n')

    return f.name


def test_good_file_length(short_file):
    assert file_length(short_file) == 10


def test_bad_file_length():
    with pytest.raises(Exception):
        file_length('/etcccc/adfsa')
