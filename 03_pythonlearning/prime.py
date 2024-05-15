def is_prime(number):
    temp_value = None

    if number < 0 or number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            temp_value = False 

    if temp_value == None:    
        return True 
    else:
        return False


