# Exercise: List Filtering 

# Instruction:
"""In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

Example
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]"""

# Solution:
def filter_list(list):
    """Retuns a list which contains non-negative integer values"""
    # Uses list comprehension and if ternary operation 
    # for better code readability

    # Uses built-in function called 'type()', which returns 
    # the type of a object
    return [elem for elem in list if type(elem) == int]