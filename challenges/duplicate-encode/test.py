"""Unit testing is a software testing method by which individual units of source code are put under
various tests to determine whether they are fit to use (Source). It determines and ascertains the
quality of your code. 

The unit test framework in Python is called unittest, which comes packaged with Python.

The unittest unit testing framework was originally inspired by JUnit and has a similar flavor 
as major unit testing framework in other languages. It supports test automation, sharing of 
setup and shutdown code for tests, aggregation of tests into collections, and independence of
the tests from the reporting framework."""

import unittest
from app import duplicate_encode
from app import duplicate_encode_refactored

class TestMethod(unittest.TestCase):

    def test_function(self):
        """Syntax: assertEqual(firstValue, secondValue, message)

        Parameters: assertEqual() accept three parameter which are listed below with explanation:

        firstValue  variable of any type which is used in the comparison by function
        secondValue: variable of any type which is used in the comparison by function
        message: a string sentence as a message which got displayed when the test case got failed."""
        self.assertEqual(duplicate_encode("Summer"), "(())((")
        self.assertEqual(duplicate_encode_refactored("recede"), "()()()")
        self.assertEqual(duplicate_encode("succeed"), "(())))(")
        self.assertEqual(duplicate_encode_refactored("seeds"), ")))()")
        self.assertEqual(duplicate_encode("Warriors"), "(())(()(")
        self.assertEqual(duplicate_encode_refactored("Elements"), ")()()(((")
        
if __name__ == "__main__":
    """if __name__ == “main”: is used to execute some code only if the file was run 
    directly, and not imported.

    Some useful links:
    - https://www.freecodecamp.org/news/if-name-main-python-example/
    - https://codefather.tech/blog/if-name-main-python/
    
    run in terminal: python test.py
    
    Passing the -v option to your test script will instruct unittest.main()
    to enable a higher level of verbosity, and produce a more detailed test output
     
    run in terminal: python test.py -v is equivalent to unittest.main(verbosity=1)"""
    
    unittest.main(verbosity=2)