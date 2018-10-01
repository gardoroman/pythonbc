import unittest
import cap


class TestCap(unittest.TestCase):

    def test_one_word(self):
        text = 'python'
        result = cap.cap_text(text)
        self.assertEqual(result, 'Python')

    def test_multiple_words(self):
        words = 'capitalized words'
        res = cap.cap_text(words)
        self.assertEqual(res, 'Capitalized Words')

    def test_with_apostrophes(self):
        words = "well you needn't"
        res = cap.cap_text(words)
        self.assertEqual(res, "Well You Needn't")


if __name__ == '__main__':
    unittest.main()
