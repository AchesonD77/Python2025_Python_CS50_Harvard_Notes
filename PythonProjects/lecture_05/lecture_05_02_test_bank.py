"""
from bank import value
→ This imports the value() function from your main program, without executing main().

Why use assert?
An assertion checks that your code behaves correctly.
For example:
assert value("hello") == 0
If it’s true → test passes
If false → test fails, pytest will show the mismatch.

Function naming rule
Every test must start with test_, otherwise pytest won’t find it.

Python Concepts You Learned Here
Concept	Meaning / Example
def	defines a function
input()	reads user input as a string
lower()	converts text to lowercase
startswith()	checks how a string begins
if / elif / else	conditional branching
return	gives back a value from a function
assert	test that a condition is true
pytest	testing framework to automate checks
__name__ == "__main__"	ensures code runs only when directly executed
"""


from bank import value


def test_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("hello there") == 0


def test_h_only():
    assert value("hi") == 20
    assert value("Hey") == 20
    assert value("hola") == 20


def test_other():
    assert value("good morning") == 100
    assert value("good afternoon") == 100
    assert value("what's up") == 100

