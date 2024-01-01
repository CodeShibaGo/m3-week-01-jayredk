def find_smallest_int(arr):
    ans = arr[0]
    for num in arr:
        ans = min(ans, num)
    return ans
    pass
