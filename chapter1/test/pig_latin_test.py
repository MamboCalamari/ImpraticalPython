from unittest import TestCase
from chapter1.pig_latin import translate_word, translate_sentence


class PigLatinTest(TestCase):
    def test_vowel_word(self):
        assert "okayway" == translate_word("okay")

    def test_consonant_word(self):
        assert "openay" == translate_word("nope")

    def test_mixed_sentence(self):
        print(translate_sentence("This is a sentence."))
        assert "Histay isway away entencesay." == translate_sentence("This is a sentence.")
