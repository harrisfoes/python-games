def main():
    book_path  = 'books/frankenstein.txt'
    contents = open_book(book_path)
    print(contents)
    print(count_words(contents))


def open_book(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)


main()
