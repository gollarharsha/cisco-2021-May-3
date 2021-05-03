def firstlast(seq):
    if not seq:
        return seq

    return seq[:1] + seq[-1:]

    if isinstance(seq, str):
        return seq[0] + seq[-1]

    elif isinstance(seq, list):
        return [seq[0], seq[-1]]

    elif isinstance(seq, tuple):
        return (seq[0], seq[-1])

    else:
        raise TypeError('Not a sequence!')
