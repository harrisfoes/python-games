def find_min(nums):
    min = float("inf")
    
    for num in nums:
        if num < min:
            min = num

    return min

