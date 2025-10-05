"""
You must write a program in a file called fuel.py that:
Prompts the user for a fraction in the form X/Y.
Both X and Y are positive integers.
Example inputs: 1/4, 3/4, 2/3, etc.
Converts that fraction into a percentage of fuel left in the tank.

Outputs:
"E" if ≤ 1% (essentially empty)
"F" if ≥ 99% (essentially full)
Otherwise, print the percentage rounded to the nearest integer (e.g., 75%)
Must handle invalid input gracefully — if the user types nonsense, re-prompt until correct.
Catch exceptions like ValueError and ZeroDivisionError.

python concepts:
Concept	Meaning
try ... except
Handle runtime errors without crashing.
split()
Split a string like "3/4" into ["3", "4"].
int()
Convert string numbers to integers.
round()
Round a float to the nearest integer.
while True:
Create a loop that continues until valid input is entered.
return
End the function and give back a value.
"""


def main():
    fraction = get_fraction()
    percentage = round(fraction * 100)

    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")


def get_fraction():
    while True:
        try:
            x, y = input("Fraction: ").split("/")
            x = int(x)
            y = int(y)
            # check that x and y are positive and valid, Avoid division by zero, Invalid if numerator > denominator
            if y == 0 or x > y or x < 0 or y < 0:
                continue

            return x / y
        except ValueError:
            # Handles invalid integers or non-numeric input
            pass
        except ZeroDivisionError:
            # Handles division by zero (redundant but safe)
            pass

if __name__ == '__main__':
    main()