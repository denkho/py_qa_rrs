def distinct(seq):
    res_seq = []
    for element in seq:
        if element not in res_seq:
            res_seq.append(element)
    return res_seq
    # return sorted(set(seq), key = seq.index) # решение

print(distinct([1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7]))