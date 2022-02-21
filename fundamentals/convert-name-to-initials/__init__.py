from app import (abbrev_name,
            refac_abbrev_name)

if __name__ == "__main__":
    """if __name__ == “main”: is used to execute some code only if the file was run 
    directly, and not imported.

    Some useful links:
    - https://www.freecodecamp.org/news/if-name-main-python-example/
    - https://codefather.tech/blog/if-name-main-python/"""

    print(abbrev_name('Sam Witwicky'))
    print(refac_abbrev_name('Sam Witwicky'))