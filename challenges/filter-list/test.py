from app import filter_list
import unittest

class TestMethod(unittest.TestCase):

    def test_func(self):
        self.assertEqual(filter_list([1,2,'a','b']),[1,2])
        self.assertEqual(filter_list([1,'a','b',0,15]),[1,0,15])
        self.assertEqual(filter_list([1,2,'aasf','1','123',123]),[1,2,123])

if __name__ == "__main__":
    """if __name__ == “main”: is used to execute some code only if the file was run 
    directly, and not imported.

    Some useful links:
    - https://www.freecodecamp.org/news/if-name-main-python-example/
    - https://codefather.tech/blog/if-name-main-python/"""
    
    unittest.main(verbosity=2)