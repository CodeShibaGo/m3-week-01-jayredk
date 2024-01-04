def calculate_average(nums):
    sum = 0
    totalNum = 0
    
    for num in nums:
        sum += num
        totalNum += 1
    return sum / totalNum
