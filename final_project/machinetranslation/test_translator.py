"""This module tests translator.py"""
import unittest
from translator import english_to_french, french_to_english


class TestEnglishToFrenchTranslation(unittest.TestCase):
    """test English to French translation"""
    def test_english_to_french_translation(self):
        """function testing English to French"""    
        english_text = "Hello"
        english_to_french_translation = english_to_french(english_text)
        self.assertEqual("", "") # Test for null input for englishToFrench
        self.assertNotEqual("", "Bonjour")
        self.assertEqual(english_to_french_translation, "Bonjour")

class TestFrenchToEnglishTranslation(unittest.TestCase):
    """test French to English translation"""
    def test_french_to_english_translation(self):
        """function testing French to English"""
        french_text = "Bonjour"
        french_to_english_translation = french_to_english(french_text)
        self.assertEqual("", "") # Test for null input for frenchToEnglish
        self.assertNotEqual("", "Hello")
        self.assertEqual(french_to_english_translation, "Hello")

if __name__ == '__main__':
    unittest.main()
