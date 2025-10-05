"""
Python dictionaries, string methods, sorting, loops, and exception handling.


Problem Summary
You will:
Continuously ask the user for grocery items (one per line).
Stop when the user presses Ctrl+D (end of input).
Count how many times each item was entered.

Finally, print the list:
All item names in uppercase.
Sorted alphabetically.
Each line prefixed by its count.


Step 1. Think About the Tools You Need
We’ll use:
Concept	Description	Example:
Dictionary	Stores each item as a key and its count as the value	{"apple": 2, "banana": 1}
Loop	To keep reading input until user ends	while True:
Exception Handling	To catch Ctrl+D (EOFError)	except EOFError:
String Methods	To normalize case	.lower() or .upper()
Sorting	To print items alphabetically	for item in sorted(dict):


Start with an empty dictionary
Read user input in a loop
Explanation:
.strip() removes extra spaces.
.lower() ensures case-insensitive counting.
If the item already exists → add 1
Otherwise → create it with value 1.

Step 3. Print the Result (sorted alphabetically)
sorted(grocery_list) gives an alphabetically sorted list of dictionary keys.
.upper() prints item names in all uppercase.


Knowledge Recap
Concept	Explanation	Example
Dictionary	Key-value structure for storing counts	{"milk": 1, "apple": 2}
Infinite loop	Keeps prompting user until exit	while True:
Exception Handling	Captures Ctrl+D without crashing	except EOFError:
String .lower()	Ensures all inputs are counted equally	"Apple".lower() → "apple"
String .upper()	Prints all items in uppercase	"apple".upper() → "APPLE"
Sorted()	Alphabetically sorts keys	sorted(["banana","apple"]) → ["apple","banana"]
f-string formatting	Makes printed output readable	f"{count} {item.upper()}"
"""


def main():
    grocery_list = {

    }

    while True:
        try:
            item = input().strip().lower() # ignore spaces and lowercase
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1
        except EOFError:
            break

    for item in sorted(grocery_list):
        print(f"{grocery_list[item]} {item.upper()}")


if __name__ == '__main__':
    main()

