from datetime import date
from seasons import minutes, to_english

def test_minutes_simple():
    # One day difference = 1440 minutes
    assert minutes(date(2000, 1, 1), date(2000, 1, 2)) == 1440

def test_minutes_zero():
    assert minutes(date(2025, 1, 1), date(2025, 1, 1)) == 0

def test_words_sample():
    # Famous line from Rent: 525,600 minutes
    assert to_english(525600) == "Five hundred twenty-five thousand, six hundred minutes"
