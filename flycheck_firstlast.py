def firstlast(seq):
    if not seq:
        return seq
    
    if isinstance(seq, str):
        return seq[0] + seq[-1]

    elif isinstance(seq, list):
        return seq[