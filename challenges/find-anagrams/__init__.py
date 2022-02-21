from app import (anagrams, 
            refac_anagrams)

if __name__ == "__main__":
    """if __name__ == “main”: is used to execute some code only if the file was run 
    directly, and not imported.

    Some useful links:
    - https://www.freecodecamp.org/news/if-name-main-python-example/
    - https://codefather.tech/blog/if-name-main-python/"""
    
    # For anagrams function
    print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))

    # For refac_anagrams function
    print(refac_anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))