"""Unit testing is a software testing method by which individual units of source code are put under
various tests to determine whether they are fit to use (Source). It determines and ascertains the
quality of your code. 

The unit test framework in Python is called unittest, which comes packaged with Python.

The unittest unit testing framework was originally inspired by JUnit and has a similar flavor 
as major unit testing framework in other languages. It supports test automation, sharing of 
setup and shutdown code for tests, aggregation of tests into collections, and independence of
the tests from the reporting framework."""

import unittest
from app import alphabet_position_refactored

class TestCases(unittest.TestCase):
    
    def test_function(self):
        """Syntax: assertEqual(firstValue, secondValue, message)

        Parameters: assertEqual() accept three parameter which are listed below with explanation:

        firstValue  variable of any type which is used in the comparison by function
        secondValue: variable of any type which is used in the comparison by function
        message: a string sentence as a message which got displayed when the test case got failed."""
        self.assertEqual(alphabet_position_refactored("gullible"), "7 21 12 12 9 2 12 5")
        self.assertEqual(alphabet_position_refactored("transfer"), "20 18 1 14 19 6 5 18")
        self.assertEqual(alphabet_position_refactored("advertisement"), "1 4 22 5 18 20 9 19 5 13 5 14 20")

    def test_function_with_capitals(self):
        """Syntax: assertEqual(firstValue, secondValue, message)

        Parameters: assertEqual() accept three parameter which are listed below with explanation:

        firstValue  variable of any type which is used in the comparison by function
        secondValue: variable of any type which is used in the comparison by function
        message: a string sentence as a message which got displayed when the test case got failed."""
        self.assertEqual(alphabet_position_refactored("GULLIBLE"), "7 21 12 12 9 2 12 5")
        self.assertEqual(alphabet_position_refactored("Transfer"), "20 18 1 14 19 6 5 18")
        self.assertEqual(alphabet_position_refactored("ADVERTISEMENT"), "1 4 22 5 18 20 9 19 5 13 5 14 20")

if __name__ == "__main__":
    """if __name__ == “main”: is used to execute some code only if the file was run 
    directly, and not imported.

    Some useful links:
    - https://www.freecodecamp.org/news/if-name-main-python-example/
    - https://codefather.tech/blog/if-name-main-python/
    
    run in terminal: python test.py
    
    Passing the -v option to your test script will instruct unittest.main()
    to enable a higher level of verbosity, and produce a more detailed test output
     
    run in terminal: python test.py -v is equivalent to unittest.main(verbosity=1)
    
    Level of verbosity: 
        0 (quiet): you just get the total numbers of tests executed and the global result
        1 (default): you get the same plus a dot for every successful test or a F for every failure
        2 (verbose): you get the help string of every test and the result"""
    unittest.main(verbosity=2)