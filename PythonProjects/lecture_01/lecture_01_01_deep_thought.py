# 1. input()
# Prompts the user and returns a string.
# 2. .strip()
# Removes extra spaces before/after the input.
# Removes accidental spaces:
# " 42 ".strip() → "42"
# 3. .lower()
# Makes the string lowercase → easier to compare ignoring case.
# .lower() ensures case-insensitive comparison.
# 4. if statements
# Conditional checks in Python.

def main():
    answer = (input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")).strip().lower()
    if answer == "42" or answer == 'forty-two' or answer == 'forty two':
        print("Yes")
    else:
        print("No")


main()
