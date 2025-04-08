import unittest
from textcleaner import clean_sentence

class TestCleanSentence(unittest.TestCase):
    def test_cleaning(self):
        sentence = "Hello, hello world! Clean clean."
        expected = ['clean', 'hello', 'world']
        self.assertEqual(clean_sentence(sentence), expected)

    def test_case_insensitive(self):
        sentence = "This is THIS is."
        expected = ['is', 'this']
        self.assertEqual(clean_sentence(sentence), expected)

    def test_empty_input(self):
        self.assertEqual(clean_sentence(""), [])

if __name__ == '__main__':
    unittest.main()
