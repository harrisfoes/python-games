def count_vowels(text):
    n_vowels = 0
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    unique_vowels = set()

    for letter in text:
        if letter in vowels:
            n_vowels = n_vowels + 1
            unique_vowels.add(letter)

    return n_vowels, unique_vowels

