# Exercise: Replace With Alphabet Position

# Instruction: 
"""In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.

Example
alphabet_position("The sunset sets at twelve o' clock.")
Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )"""

# Solution: 
def alphabet_position(text):
    result = ""
    dict_alphabet = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12, "m": 13, "n": 14, "o": 15, "p": 16, "q": 17, "r": 18, "s": 19, "t": 20, "u": 21, "v": 22, "w": 23, "x": 24, "y": 25, "z": 26}
    for x in text.lower():
        if x in dict_alphabet.keys():
            result += str(dict_alphabet[x]) + " "
    return result[:len(result) - 1]

# Refactored Solution 1: 
def alphabet_position_refactored(text):
    text = text.lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Longer version
    # letter_to_number = []

    # for pos in range(len(text)):
    #     for letter in alphabet:
    #         if text[pos] == letter:
    #             alphabet.index(letter)
    # return letter_to_number

    # Shorter version: using list comprehension and ternary operator to form a new list object
    return ' '.join([str(alphabet.index(letter) + 1) for pos in range(len(text)) for letter in alphabet if text[pos] == letter])
