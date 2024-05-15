def get_champion_slices(champions):    
    value1 = champions[2:]
    value2 = champions[:-2]
    value3 = champions[::2]
    return value1, value2, value3




    #First, return a slice of the champions list that starts with the third champion and goes to the end of the list.
    #Next, return a slice of the champions list that starts at the beginning of the list and ends with the third champion from the end (inclusive).
    #Last, return a slice of the champions list that only includes the champions in even numbered indexes.

