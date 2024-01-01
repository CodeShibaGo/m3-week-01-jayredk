def array_diff(a, b):
    arr = []
    for el in a:
        if el in b:
            continue
        arr.append(el)
    return arr