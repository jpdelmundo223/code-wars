# Exercise: Odd or Even?

# Instructions:
"""Given a list of integers, determine whether the sum of its elements is odd or even.

Give your answer as a string matching "odd" or "even".

If the input array is empty consider it as: [0] (array with a zero).

Examples:
Input: [0]
Output: "even"

Input: [0, 1, 4]
Output: "odd"

Input: [0, -1, -5]
Output: "even"
Have fun!"""

# Solution:
def odd_or_even(arr):
    """Function that determines whether the sum of the 
    given array is odd or even
    
    :param arr: holds the value of array"""
    
    sum = 0
    for i in arr:
        sum += i
    if sum % 2 == 0:
        return "even"
    return "odd"

# Refactored Solution:
def refac_odd_or_even(arr):
    """Function that determines whether the sum of the 
    given array is odd or even
    
    :param arr: holds the value of array"""

    return "even" if sum(arr) % 2 == 0 else "odd"