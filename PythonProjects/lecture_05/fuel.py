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
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError):
            pass


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


def convert(fraction):
        try:
            x, y = fraction.split("/")
            x = int(x)
            y = int(y)
        except (ValueError, AttributeError):
            raise ValueError("Invalid input format")


        # check that x and y are positive and valid, Avoid division by zero, Invalid if numerator > denominator
        if y == 0:
            raise ZeroDivisionError("Denominator cannot be zero")
        if x > y:
            raise ValueError("Numerator cannot be greater than denominator")

        percentage = round((x / y) * 100)
        return  percentage


if __name__ == '__main__':
    main()