# Exercise: Where's my anagrams at?

# Instructions: 
"""What is an anagram? Well, two words are anagrams of each other if they both contain the same letters. For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false
Write a function that will find all the anagrams of a word from a list. You will be given two inputs a word and an array with words. You should return an array of all the anagrams or an empty array if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []
Note for Go
For Go: Empty string slice is expected when there are no anagrams found."""

# Logic:
"""What is an Anagram?
    Anagrams are words or phrases you spell by rearranging the 
    letters of another word or phrase. For instance, fans of the
    Harry Potter series know that Lord Voldemort’s full name is
    actually an anagram of his birth name, and some people even
    play games challenging one another to make anagrams still 
    relevant to the original term. For example, "schoolmaster"
    can be turned into "the classroom", "punishments" becomes 
    "nine thumps", and "debit card" turns into "bad credit".

    The only rule is that all the letters from the original word 
    or phrase must be used when they’re reordered to say something 
    entirely different.
    """

# Solution:
def anagrams(word, words):
    """Returns a list of words that if sorted, results to
    being an equivalent of the first parameter(word)
    
    :param word: this holds the compare value
    :param words: this holds the list of value to be compared with"""

    # Variable that will be used to temporarily hold list of values
    # that if each characters is checked one by one, matches all
    # the letters in the word parameter (of array/list object)
    temp_list = []
    # Variable that will hold the last/final result (of array/list object)
    res = []
    # Iterates through the given list
    for x in words:
        # Validates if length of x (words.index(x)) is greater than '>'
        # the length of word then returns true and will skip the 
        # current value of x
        if not len(x) > len(word):
            # Iterates throught the series of letter in parameter word,
            # which then validates if char is in x (words.index(x))
            for char in x:
                # If validation returns False, clears the temp_list
                if char in word:
                    for y in word:
                        if y in x:
                            temp_list.append(x)
                        else:
                            temp_list.clear()
                            # breaks the loop
                            break
                else:
                    temp_list.clear()
                    # breaks the loop
                    break
            # Cancels append if temp_list is empty or zero
            if not len(temp_list) == 0:
                # Uses .join() to concatenate list that separates with ''
                res.append(''.join(set(temp_list)))
            # Clears the temp_list every time a loop finishes
            # to avoid duplicates in the result
            temp_list.clear()
    # Finally, returns the final result
    return res

# Refactored Solution:
def refac_anagrams(word, words):
    """Returns a list of words that if sorted, results to
    being an equivalent of the first parameter(word)
    
    :param word: this holds the compare value
    :param words: this holds the list of value to be compared with"""

    # Uses the built-in function sorted(), which return a
    # new sorted list from the items in iteratable (can be of type string, lists, sets, or dict.)

    # Returns a list of words, that matches the first parameter
    # after being sorted.
    return [w for w in words if sorted(w) == sorted(word)]