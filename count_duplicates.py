def count_duplicates(text):
    dict = {}
    duplicateSet = set()

    for char in text:
        c = char.lower()
        if c in dict:
            duplicateSet.add(c)
        elif c not in dict:
            dict[c] = 1

    return len(duplicateSet)