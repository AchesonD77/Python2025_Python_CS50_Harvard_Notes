"""
Task
In twttr.py:
Prompt the user for a string of text.
Output the same text but without vowels (a, e, i, o, u in both upper and lower case).

1. input()
Ask the user:
text = input("Input: ")

2. For loop (iterate over string)
We’ll check each character:
for c in text:
    ...

3. Condition (if)
Skip vowels:
if c.lower() not in "aeiou":
    ...

4. Building output
We can either:
Print directly inside the loop, OR
Build a new string and print at the end.


Why c.lower()?
We want case-insensitive comparison.
"A".lower() → "a", so it matches vowels in "aeiou".

Why build a string?
Strings are immutable in Python (cannot be modified in place).
We construct a new string by concatenation (result += c).

"".join([...])
Joins the list back into a string with no spaces between elements.
"""


def main():
    text = input("Input: ")
    print("output: ", remove_vowels(text))


# we give a string to be the argument
def remove_vowels(string):
    result = ""
    for c in string:
        if c.lower() not in "aeiuo":
            result += c
    return result
"""
def remove_vowels(s):
    return "".join([c for c in s if c.lower() not in "aeiou"])
"""

if __name__ == "__main__":
    main()

    '''
    if __name__ == "__main__": main() = the switch that decides whether your program should run immediately, 
    or just quietly provide tools to other programs.'''