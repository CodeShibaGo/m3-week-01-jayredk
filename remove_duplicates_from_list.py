def distinct(seq):
    num_set = set()
    arr = []
    
    for num in seq:
        if num in num_set:
            continue
        else:
            num_set.add(num)
            arr.append(num)
    return arr