from app import (abbrev_name
            , refac_abbrev_name)
import unittest

class TestMethod(unittest.TestCase):

    def test_abbrev_name(self):
        self.assertEqual(abbrev_name("Sam Harris"), "S.H")
        self.assertEqual(abbrev_name("patrick feenan"), "P.F")
        self.assertEqual(abbrev_name("Evan C"), "E.C")
        self.assertEqual(abbrev_name("P Favuzzi"), "P.F")
        self.assertEqual(abbrev_name("David Mendieta"), "D.M")

    def test_refac_abbrev_name(self):
        self.assertEqual(refac_abbrev_name("Sam Harris"), "S.H")
        self.assertEqual(refac_abbrev_name("patrick feenan"), "P.F")
        self.assertEqual(refac_abbrev_name("Evan C"), "E.C")
        self.assertEqual(refac_abbrev_name("P Favuzzi"), "P.F")
        self.assertEqual(refac_abbrev_name("David Mendieta"), "D.M")

if __name__ == "__main__":
    """if __name__ == “main”: is used to execute some code only if the file was run 
    directly, and not imported.

    Some useful links:
    - https://www.freecodecamp.org/news/if-name-main-python-example/
    - https://codefather.tech/blog/if-name-main-python/"""

    unittest.main(verbosity=2)