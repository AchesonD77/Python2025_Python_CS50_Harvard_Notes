"""
:( test_plates catches plates.py without beginning alphabetical checks
    expected exit code 1, not 0

Your test suite did not catch the specific error where a license plate doesn’t start with two letters.

However, all of these are invalid for multiple reasons, not just because they don’t begin with two letters.
For example:
"50CS" fails also because numbers come first (invalid number placement).
"C5S0" fails also because letters appear after numbers.
"5S" fails both because it starts with a number and length < 2.
So even a buggy version of plates.py (that forgets to check the “two letters first” rule)
would still reject these inputs for other reasons — making your test suite blind to that missing rule.

To fix this, we added tests that:
Obey all other rules (length, alphanumeric, number placement, zero rule),
But break only the “must begin with two letters” rule.

These examples are crucial because:
They have valid lengths (2–6),
Contain only letters/numbers,
Numbers are at the end,
No leading zero,
👉 So the only reason they should fail is the “start with two letters” rule.

Concept taught: isolate one rule and test only that condition (unit testing best practice).


What You Learned About Python Testing
Concept	Explanation
assert	Verifies whether a condition is True. If False, the test fails.
pytest discovery	pytest automatically runs any function that starts with test_.
Unit testing	Each test checks one logical rule separately.
Regression testing	Tests protect against future mistakes (if you modify code later).
Edge cases	Tests must include minimal or special inputs (like “A1”) to catch hidden bugs.
"""


from plates import is_valid


def test_length():
    assert is_valid("A") is False
    assert is_valid("ABCDEFG") is False
    assert is_valid("CS50") is True


def test_starts_with_two_letters_only_rule():
    assert is_valid("A1") is False
    assert is_valid("C123") is False
    assert is_valid("AB123") is True


def test_starts_with_letters_others():
    assert is_valid("50CS") is False   # numbers before letters
    assert is_valid("C5S0") is False   # letters after digits
    assert is_valid("5S") is False
    assert is_valid("CS50") is True


def test_numbers_position():
    assert is_valid("CS50P") is False  # letters after digits
    assert is_valid("CS05") is False   # first digit is zero
    assert is_valid("CS50") is True


def test_only_alphanumeric():
    assert is_valid("CS50!") is False
    assert is_valid("CS 50") is False
    assert is_valid("CS50") is True
