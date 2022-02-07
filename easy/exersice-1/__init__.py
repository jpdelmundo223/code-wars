from app import duplicate_encode
from app import duplicate_encode_refactored
text = "The quick brown fox jumps over the lazy dog."

if __name__ == "__main__":
    # runs the py application
    print(duplicate_encode(text))
    print(duplicate_encode_refactored(text))