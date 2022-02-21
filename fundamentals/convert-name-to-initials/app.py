# Exercise: Abbreviate a Two Word Name

# Instructions:
"""Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F"""

# Solution:
def abbrev_name(name):
    """Returns the abbreviation of a two word name.
    
    :param name: initial argument that be taken and converted 
    to it's abbreviation"""

    # Variable of type(list), that will hold
    # the final result
    result = []
    # Iterates and get all the words after every whitespace
    for i in name.split(' '):
        # Converts i first letter/character to
        # upper case then append to result
        result.append(i[0].upper())
    # Finally returns the result
    return '.'.join(result)

# Refactored Solution:
def refac_abbrev_name(name):
    """Returns the abbreviation of a two word name.
    
    :param name: initial argument that be taken and converted 
    to it's abbreviation"""

    # Shorter method
    if len(name.split(' ')) > 2:
        return "Function don't accept input that is more than 2 words!"
    return '.'.join([i[0].upper() for i in name.split(' ')])
    