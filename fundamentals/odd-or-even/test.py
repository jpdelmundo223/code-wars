from app import (odd_or_even,
            refac_odd_or_even)
import unittest

class TestMethod(unittest.TestCase):

    def test_odd_or_even(self):
        self.assertEqual(odd_or_even([0, 1, 2]), "odd")
        self.assertEqual(odd_or_even([0, 1, 3]), "even")
        self.assertEqual(odd_or_even([1023, 1, 2]), "even")

    def test_refac_odd_or_even(self):
        self.assertEqual(refac_odd_or_even([0, 1, 2]), "odd")
        self.assertEqual(refac_odd_or_even([0, 1, 3]), "even")
        self.assertEqual(refac_odd_or_even([1023, 1, 2]), "even")        

if __name__ == "__main__":
    """if __name__ == “main”: is used to execute some code only if the file was run 
    directly, and not imported.

    Some useful links:
    - https://www.freecodecamp.org/news/if-name-main-python-example/
    - https://codefather.tech/blog/if-name-main-python/"""
    
    unittest.main(verbosity=2)