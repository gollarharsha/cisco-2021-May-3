def add_numbers():
    s = input('Enter numbers, separated by whitespace: ').strip()
    first, second = s.split()
    return int(first) + int(second)
