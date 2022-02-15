# Exercise: Roman Numerals Decoder

# Instruction: 
"""Create a function that takes a Roman numeral as its argument and returns its value as a numeric decimal integer. You don't need to validate the form of the Roman numeral.

Modern Roman numerals are written by expressing each decimal digit of the number to be encoded separately, starting with the leftmost digit and skipping any 0s. So 1990 is rendered "MCMXC" (1000 = M, 900 = CM, 90 = XC) and 2008 is rendered "MMVIII" (2000 = MM, 8 = VIII). The Roman numeral for 1666, "MDCLXVI", uses each letter in descending order.

Example:

solution('XXI') # should return 21
Help:

Symbol    Value
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000"""

# Solution:
def solution(roman):
    """Converting Roman Numerals to Number Rules / Logic: (https://www.mathsisfun.com/roman-numerals.html)

    When a symbol appears 'after' a larger (or equal) symbol it is added
    Example: [VI] = V + I = (5 + 1) = 6
    Example: [LXX] = L + X + X = (50 + 10 + 10) = 70

    But if the symbol appears 'before' a larger symbol it is subtracted
    Example: [IV] = V - I = (5 - 1) = 4
    Example: [IX] = X - I = (10 - 1) = 9

    To Remember:
    Don't use the same symbol more than three times in a row (but IIII is sometimes used for 4, particularly on clocks)
    """
    roman_dict = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
    roman = roman.upper()
    prev_val = 0
    res = 0

    for x in range(len(roman)):
        for key, val in roman_dict.items():
            if roman[x] == key:
                try:
                    if val < roman_dict[roman[x + 1]]:
                        prev_val = val
                    else:
                        res += val
                        prev_val = 0
                    res -= prev_val
                except:
                    res += val
    return res