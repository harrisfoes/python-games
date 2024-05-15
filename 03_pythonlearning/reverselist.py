def reverse_array(items):
    new_array = []

    for i in range(len(items) -1, -1, -1):
        new_array.append(items[i])

    return new_array;



