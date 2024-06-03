def factorial(num):
    result = num

    if num == 0:
        return 1

    for n in reversed(range(num)):
        if n > 0:
            result = result * n
    
    return result

