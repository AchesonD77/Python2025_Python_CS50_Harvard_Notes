
from twttr import remove_vowels


def test_basic():
    assert remove_vowels("Twitter") == "Twttr"
    assert remove_vowels("Hello") == "Hll"
    assert remove_vowels("CS50") == "CS50"


def test_upper_lower_mix():
    assert remove_vowels("AeIouU") == ""
    assert remove_vowels("Programming") == "Prgrmmng"


def test_with_punctuation():
    assert remove_vowels("What's up?") == "Wht's p?"
    assert remove_vowels("I love, Python!") == " lv, Pythn!"

