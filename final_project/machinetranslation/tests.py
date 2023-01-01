import unittest
from translator import english_to_french,french_to_english

class TestenglishToFrench(unittest.TestCase):
     def test_1(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour") 
        self.assertEqual(english_to_french("Hello world"),"Bonjour le monde")
        self.assertNotEqual(english_to_french("Bye"),"Bonjour")
        self.assertEqual(english_to_french(""),"")
        self.assertEqual(english_to_french("--"),"--")

class TestfrenchToEnglish(unittest.TestCase):
    def test_2(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        self.assertEqual(french_to_english("Grand ours"),"Great Bear")
        self.assertNotEqual(french_to_english("Ciel gris"),"White skies")
        self.assertEqual(french_to_english(""),"")
        self.assertEqual(french_to_english("--"),"--")
       

if __name__== "__main__":
     unittest.main()
  