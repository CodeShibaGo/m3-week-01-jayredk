def categorize_new_member(data):
    arr = []

    for el in data:
        age = el[0]
        contribution = el[1]

        if age >= 55 and contribution > 7:
            arr.append('Senior')
        else:
            arr.append('Open')
    return arr