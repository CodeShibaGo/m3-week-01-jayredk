def unique_in_order(iterable):
    arr = []
    if (len(iterable) == 0):
        return arr
        
    arr = [iterable[0]]
    index = 0

    for el in iterable:
        if el != arr[index]:
            arr.append(el)
            index += 1
            
    return arr
    pass