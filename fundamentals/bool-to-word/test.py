from app import bool_to_word
import unittest

class TestMethod(unittest.TestCase):

    def test_func(self):
        self.assertEqual(bool_to_word(False), 'No')
        self.assertEqual(bool_to_word(True), 'Yes')

if __name__ == "__main__":
    """if __name__ == “main”: is used to execute some code only if the file was run 
    directly, and not imported.

    Some useful links:
    - https://www.freecodecamp.org/news/if-name-main-python-example/
    - https://codefather.tech/blog/if-name-main-python/"""
    
    unittest.main(verbosity=2)