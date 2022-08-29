import unittest

from translator import english_to_french, french_to_english

class TestenglishToFrench(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(english_to_french("None"),'') #test for null input
        self.assertEqual(english_to_french('Hello'),'Bonjour') #test when Hello is input

class TestfrenchtoEnglish(unittest.TestCase):
    def test1(self):
        self.assertNotEqual(french_to_english("None"),'') #test for null input
        self.assertEqual(french_to_english('Bonjour'),'Hello') #test when Bonjour is input

unittest.main()