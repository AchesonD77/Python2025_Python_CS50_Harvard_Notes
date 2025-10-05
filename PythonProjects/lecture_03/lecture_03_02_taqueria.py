"""
use Python dictionaries, loops, string methods, and exception handling to build an interactive program.


Problem Overview
You need to:
Prompt the user repeatedly to input an item name from a menu.
Keep a running total of the cost of valid items.
When the user ends input (with Ctrl+D on macOS/Linux or Ctrl+Z on Windows), print the total price formatted like $12.50.


Step 1. Build the Menu:
In Python, a dictionary (dict) stores key-value pairs.
Here, the key is the item name and the value is its price.
Concepts used:
A dict maps keys (like "Taco") to values (like 3.00).
Access a value by key: menu["Taco"] → 3.00
Add up the total using arithmetic with these float values.

Step 2. Take User Input Repeatedly
We use a loop to keep asking for input until the user stops (Ctrl+D).


while True:
This creates an infinite loop that only ends when you break it manually.

.title()
The .title() method capitalizes the first letter of each word —
so "taco" becomes "Taco", matching the dictionary key format.
This makes the input case-insensitive!

print(f"Total: ${total:.2f}")
The f-string formats the total to two decimal places (.2f = 2 digits after the decimal).

except EOFError:
The EOFError (End Of File Error) is raised when the user presses Ctrl+D.
We catch it to exit the loop gracefully and print the final total.


Key Python Knowledge Recap
Concept	Example	Explanation
Dictionary	menu = {"Taco": 3.00}	Stores key-value pairs
Loop	while True:	Repeats until break
Condition	if item in menu:	Checks if input exists
Error Handling	except EOFError:	Graceful exit on Ctrl+D
f-string	f"${total:.2f}"	Formats to 2 decimals
String Method	.title()	Capitalizes properly
"""


def main():
    menu = {
        "Baja Taco": 4.25,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    total = 0

    while True:
        try:
            item = input("Item: ").title()
            if item in menu:
                total += menu[item]
                print(f"Total: ${total:.2f}")
        except EOFError:
            print()
            print(f'Total: ${total:.2f}')
            break


if __name__ == '__main__':
    main()