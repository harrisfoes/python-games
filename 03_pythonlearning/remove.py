def remove_nonints(nums):
    newlist = []

    for num in nums:
        if type(num) == int:
            newlist.append(num)

    return newlist

