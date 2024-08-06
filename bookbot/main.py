def main():
    book_path  = 'books/frankenstein.txt'
    contents = open_book(book_path)

    print(contents)

    print(f"--- Begin report of {book_path} ---")
    print(f"{count_words(contents)} words found in the document \n")

    char_dict = count_chars(contents)
    
    for key,value in char_dict.items():
        print(f"The '{key}' character was found {value} times")

    print(f"--- End report ---")


def open_book(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    dict = {}
    txt = text.lower()

    #iterate through the characters in 
    #for each new character, store it to the dict        
    #count how many of that character is in text

    for char in txt:
        if char.isalpha() and char not in dict:
            dict[char] = txt.count(char)

    return dict

def sort_count_char(dict):
    return dict["num"]



main()
