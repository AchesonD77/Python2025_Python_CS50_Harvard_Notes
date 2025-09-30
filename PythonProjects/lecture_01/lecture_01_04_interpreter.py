'''
Task
In interpreter.py:
Prompt the user for input (formatted as x y z).
x and z are integers.
y is one of + - * /.
Perform the math and print the result as a float with 1 decimal place.


input()

.split()
Splits a string into pieces based on spaces.
"1 + 1".split()  # ["1", "+", "1"]

Type Conversion
Convert strings to numbers.
int("5")  # 5

if-elif conditions
Decide which operation to perform.
if y == "+":
    result = x + z

print(f"{result:.1f}")
Format float to 1 decimal place.
print(f"{3.14159:.1f}")  # 3.1


Why .split()?
Input is always "x y z" with spaces.
.split() separates them into a list:
"8 / 2".split()  # ["8", "/", "2"]

Why int() and not float()?
The problem states x and z are integers.
But division / in Python always returns a float, which is what we need.

Why format with :.1f?
Ensures exactly 1 decimal place, even if result is whole.
Example: 2 → 2.0.
'''


def interpreter():
    expression = input("Expression: ")
    x, y, z = expression.split()
    x = int(x)
    z = int(z)

    if y == "+":
        result = x + z
    elif y == "-":
        result = x - z
    elif y == '*':
        result = x * z
    elif y == '/':
        result = x / z

    print(f"{result:.1f}")


interpreter()