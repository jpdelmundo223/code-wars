from app import duplicate_encode
from app import duplicate_encode_refactored
text = "The quick brown fox jumps over the lazy dog."

if __name__ == "__main__":
    """if __name__ == “main”: is used to execute some code only if the file was run 
    directly, and not imported.

    Some useful links:
    - https://www.freecodecamp.org/news/if-name-main-python-example/
    - https://codefather.tech/blog/if-name-main-python/"""
    print(duplicate_encode(text))
    print(duplicate_encode_refactored(text))