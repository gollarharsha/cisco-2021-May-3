def firstlast(seq):
    if not seq:
        return seq

    return seq[:1] + seq[-1:]
