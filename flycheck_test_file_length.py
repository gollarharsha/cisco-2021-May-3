from file_length import file_length


def test_good_file_length():
    assert file_length('/etc/passwd') == 7579


def test_bad_file_length():
    assert file_length('/etcccc/passwddddd') == 7579
