def age_difference(ages):
    min = 100
    max = 0
    for age in ages:
        if age > max:
            max = age
        if age < min:
            min = age
    return (min, max)
    pass