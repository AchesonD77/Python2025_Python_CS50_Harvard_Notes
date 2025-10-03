"""
Task
In plates.py, check if a user’s plate string is valid according to rules:
Must start with at least 2 letters.
Length: between 2 and 6 characters.
Numbers: if used, they must be at the end.
No letters after numbers.
The first number can’t be 0.
No periods, spaces, or punctuation marks.
Output "Valid" or "Invalid".


They gave us the platform.
We need to implement is_valid.


check each rules
Rule 1: Start with at least two letters
if not s[:2].isalpha():
    return False

s[:2] = first 2 characters.
.isalpha() checks if all are letters.

Rule 2: Length between 2 and 6
if not (2 <= len(s) <= 6):
    return False

Rule 3: Numbers only at the end
We loop through characters:
Once we hit a digit, all the rest must be digits.
Also, the first digit must not be "0".

for i, c in enumerate(s):
    if c.isdigit():
        if c == "0" and s[i:].isdigit():  # first number is zero
            return False
        if not s[i:].isdigit():  # letters after numbers
            return False
        break

Rule 4: No punctuation
if not s.isalnum():
    return False

.isalnum() = only letters and numbers allowed.


s.isalpha() → True only if all chars are letters.
s.isalnum() → True only if letters or digits, no punctuation.
enumerate(s) → lets us loop with both index and character.
for i, c in enumerate("CS50"):
    print(i, c)
0 C
1 S
2 5
3 0

the difficult thing is that we need to complete the requirement of rule: 'Also, the first digit must not be "0".'
"""


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # rule 2: len(s)
    if not (2 <= len(s) <= 6):
        return False

    # rule 1: start with at least two letters, start from 0, has 2 characters
    if not s[:2].isalpha():
        return False

    # rule 4: no punctuation
    if not s.isalnum():
        return False

    # rule 3: numbers at the end, not starting with 0
    for i, c in enumerate(s):
        if c.isdigit():
            if c == "0" and s[i:].isdigit():
                return False
            if not s[i:].isdigit():
                return False
            break
    return True


main()
