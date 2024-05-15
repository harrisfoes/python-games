def find_max(nums):
    max_so_far = float("-inf")
    for num in nums:
        print(f"{num} vs {max_so_far}")
        if num > max_so_far:
           max_so_far = num 

    return max_so_far

