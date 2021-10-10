"""
Language Translator Test Module
"""
import unittest
from translator import english_to_french, french_to_english
class Testenglishtofrench(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('0'), '0') # test for null input
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # test for words Hello and Bonjour

class Testfrenchtoenglish(unittest.TestCase):
    def test2(self):
        self.assertEqual(french_to_english('0'), '0') # test for null input
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # test for the words Bonjour and Hello

unittest.main()
