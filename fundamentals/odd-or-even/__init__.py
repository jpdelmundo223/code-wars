from app import (odd_or_even,
            refac_odd_or_even)

if __name__ == "__main__":
    """if __name__ == “main”: is used to execute some code only if the file was run 
    directly, and not imported.

    Some useful links:
    - https://www.freecodecamp.org/news/if-name-main-python-example/
    - https://codefather.tech/blog/if-name-main-python/"""
    
    print(odd_or_even([0, 1, 2]))
    print(refac_odd_or_even([0, 1, 2]))