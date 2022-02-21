from weakref import ref
from app import (anagrams, 
            refac_anagrams)
import unittest

class TestMethod(unittest.TestCase):

    # Anagrams provided by https://www.wordhelp.com/scrabble

    def test_anagrams(self):
        self.assertEqual(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
        self.assertEqual(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])
        self.assertEqual(anagrams('arms', ['mars', 'marc', 'rams', 'crams']), ['mars', 'rams'])
        self.assertEqual(anagrams('fries', ['serif', 'drief', 'fires']), ['serif', 'fires'])

    def test_refac_anagrams(self):
        self.assertEqual(refac_anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']), ['aabb', 'bbaa'])
        self.assertEqual(refac_anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']), ['carer', 'racer'])
        self.assertEqual(refac_anagrams('arms', ['mars', 'marc', 'rams', 'crams']), ['mars', 'rams'])
        self.assertEqual(refac_anagrams('fries', ['serif', 'drief', 'fires']), ['serif', 'fires'])

if __name__ == "__main__":
    unittest.main(verbosity=2)
