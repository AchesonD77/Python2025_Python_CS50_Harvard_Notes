"""
teaching you loops, lists, string joining, error handling, and conditional formatting in Python.

Python Concepts Used
Concept	Explanation	Example
List	Stores all input names	names = []
while True loop	Keeps reading input until user stops	infinite loop until break
try / except EOFError	Catches end-of-input (Ctrl+D) without crashing	except EOFError:
.append()	Adds an element to a list	names.append(name)
List slicing	Gets all but last item	names[:-1]
List indexing	Gets the last item	names[-1]
.join()	Combines list items into one string with commas	', '.join(names[:-1])
f-strings	Clean way to format text	f"{names[0]} and {names[1]}"
Function structure	Separates logic into reusable pieces	format_names()

🎓 Mini Teaching Summary
🧾 Lists hold multiple values dynamically.
🧱 While loop + try/except lets us read unknown-length input safely.
✍️ String join & f-strings are the cleanest way to build readable text.
🧩 Modular functions (like format_names) make the program organized and easy to test.
"""


def main():
    names = []

    while True:
        try:
            name = input("")
            names.append(name)
        except EOFError:
            break

    print("Adieu, adieu, to", format_names(names))


def format_names(names):
    if len(names) == 1:
        return names[0]
    elif len(names) == 2:
        return f"{names[0]} and {names[1]}"
    else:
        return f"{', '.join(names[:-1])}, and {names[-1]}"


if __name__ == '__main__':
    main()