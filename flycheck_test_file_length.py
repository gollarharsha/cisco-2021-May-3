from file_length import file_length


def check_good_file_length():
    assert file_length('/etc/passwd') == 7579
