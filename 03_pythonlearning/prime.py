def is_prime(number):
    temp_value = None

    if number < 0:
        return False
    elif number == 0 or 1:
        return False 
    
    for i in range(0, number):
        if number % i == 0:
            print(f"{number} is divisible by {i}")
            temp_value = False 

    if temp_value == None:    
        return True 
    else:
        return False

#TODO fix this shizzz
