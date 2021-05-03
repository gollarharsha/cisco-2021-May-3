def file_length(filename):
    total = 0

    for one_line in open(filename):
        total += len(one_line)

    return total
