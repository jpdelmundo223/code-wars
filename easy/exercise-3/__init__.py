from app import solution

if __name__ == "__main__":
    """if __name__ == “main”: is used to execute some code only if the file was run 
    directly, and not imported.

    Some useful links:
    - https://www.freecodecamp.org/news/if-name-main-python-example/
    - https://codefather.tech/blog/if-name-main-python/"""
    value = str(input("Enter a value: ")).upper()
    print(f"\nAnswer: {solution(value)}")