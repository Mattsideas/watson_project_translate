import unittest
from translator import english_to_french, french_to_english

class TestenglishToFrench(unittest.TestCase):
    def test(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('null'), 'null')

class TestfrenchToEnglish(unittest.TestCase):
    def test(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('null'), 'null')

if __name__=='__main__':
    unittest.main()