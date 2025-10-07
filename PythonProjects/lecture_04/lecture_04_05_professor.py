"""
How to think about it

Choose difficulty (level)
Keep asking until the user gives 1/2/3 → get_level() with while True + try/except.

Generate problems as pairs
For each of the 10 rounds: pick x and y with exact digit length using generate_integer(level).

Three attempts per problem
Loop up to 3 times. If input isn’t an int or is wrong → print "EEE".
If correct → increment score and move to next problem.

Show the answer after 3 misses
Print "{x} + {y} = {answer}".

Report total
After 10 problems, print Score: n.
"""
import random


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y

        tries = 0
        while tries < 3:
            try:
                guess = int(input(f"{x} + {y} = "))
                if guess == answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                print("EEE")
                tries += 1

        if tries == 3:
            print(f"{x} + {y} = {answer}")

    print(f"Score: {score}")



def get_level() -> int:
    # only 1,2,3
    while True:
        try:
            n = int(input("Level: "))
            if n in (1,2,3):
                return n
        except ValueError:
            pass    #repromt


def generate_integer(level: int) -> int:
    if level not in (1,2,3):
        raise ValueError('Level must be 1, 2, or 3')

    if level == 1:
        low, high = 0, 9
    else:
        low = 10 ** (level-1)
        high = 10 ** level - 1

    return random.randint(low, high)


if __name__ == '__main__':
    main()
