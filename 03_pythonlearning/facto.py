def factorial(num):
    result = 1

    for n in range(1, num):
        print(n)
        if n > 1:
            result = n * (n - 1)
            print(result, "res")
        else:
            result = 1 
    
    print(result, "final")
    return result

