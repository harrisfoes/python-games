def find_missing_ids(first_ids, second_ids): 
    #present in the first but not in second
    first_ids_set = set(first_ids)
    second_ids_set = set(second_ids)

    diff_list = list(first_ids_set - second_ids_set)

    return diff_list
