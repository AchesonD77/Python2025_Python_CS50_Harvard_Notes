"""
What you used (Python concepts)

import random + random.randint(a, b)
Picks an integer inclusive of both ends (here, from 1 to level).

Functions (get_positive_int, main)
Organize logic, avoid repetition (we validate integers in one place).

while True loops
Keep prompting until we return/break.

try / except ValueError
Safely handle non-numeric input without crashing; just reprompt.

Input validation
Require positive integers for both level and guesses (> 0).

Conditionals (if / elif / else)
Compare guess to the secret and print: Too small! / Too large! / Just right!

Note: If your checker ever complains about prompts, you can drop the prompt strings in input() (use input() instead of input("Level: ") and input("Guess: ")). The game logic stays the same.
"""


import random


def get_positive_int(prompt: str) -> int:
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
        except ValueError:
            # ask again:
            pass


def main():
    # 1. level
    level = get_positive_int("Level: ")

    # 2. pick a secret number in [1: level].
    secret = random.randint(1, level)

    # 3. keep asking until getting right
    while True:
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                continue # keep asking

            if guess < secret:
                print("Too small!")
            elif guess > secret:
                print("Too large!")
            else:
                print("Just right!")
                break
        except ValueError:
            continue


if __name__ == '__main__':
    main()