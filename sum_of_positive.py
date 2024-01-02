def positive_sum(arr):
    sum = 0
    if len(arr) == 0:
        return sum
    
    for num in arr:
        if num > 0:
            sum += num
    return sum
