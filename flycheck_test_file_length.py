import pytest
from file_length import file_length

def short_file(tmp_path):
    open(tmp_path



def test_good_file_length():
    assert file_length('/etc/passwd') == 7579


def test_bad_file_length():
    with pytest.raises(Exception):
        file_length('/etcccc/adfsa')
