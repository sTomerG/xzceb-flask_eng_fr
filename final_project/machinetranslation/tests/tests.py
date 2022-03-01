import unittest
from machinetranslation.translator import french_to_english, english_to_french

class Testfrench_to_english(unittest.TestCase):
    def test_happy(self):
        self.assertEqual(french_to_english('Bonjour'),'Hello')
        self.assertEqual(french_to_english('Maison'),'House')

    def test_null(self):
        self.assertRaises(ValueError,french_to_english,None)

class Testenglish_to_french(unittest.TestCase):
    def test_happy(self):
        self.assertEqual(english_to_french('Hello'),'Bonjour')
        self.assertEqual(english_to_french('Bye'),'Bye')
    
    def test_null(self):
        self.assertRaises(ValueError,english_to_french,None)

if __name__ == '__main__':
    unittest.main()
