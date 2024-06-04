def join_strings(strings):
    finalstring = ''
    first = True

    for string in strings:
        if first:
            finalstring = finalstring + string
            first = False
        else:
            finalstring = finalstring + ',' + string 

    return finalstring


'''

Write a function called join_strings()
that takes a list of strings and returns a single string.
Concatenate the strings from the list end-to-end, in order, with a comma between them.
Don't use the .join() string method.

Example

string_list = ["hello", "my", "friend"]
joined_string = join_strings(string_list)
print(joined_string) # "hello,my,friend"

Tip

You don't want a comma at the end or the beginning of the final string!

'''
