"""
teach you how to process files, use command-line arguments, and handle text line by line.


1️⃣ import sys
We import the sys module because it gives access to command-line arguments and the sys.exit() function.
sys.argv → a list of all command-line arguments (e.g., ["lines.py", "hello.py"]).
sys.exit() → immediately stops the program, optionally printing an error message.

2️⃣ def main():
We define a main function for organization and control flow.
You should always wrap your core logic inside main() — it keeps your code modular and testable.

3️⃣ Command-line argument check
if len(sys.argv) != 2:
    sys.exit("Too few or too many command-line arguments")

len(sys.argv) counts how many arguments the user entered.
The first argument (sys.argv[0]) is always the filename itself (lines.py).
So the user should pass exactly one additional argument (the target file to analyze).

4️⃣ File extension validation
if not filename.endswith(".py"):
    sys.exit("Not a Python file")

Here we use the string method .endswith(), which checks the file name’s suffix.
If it’s not a Python file, the program stops immediately.

5️⃣ Opening and reading the file safely
with open(filename) as file:

This uses a context manager (with) to open the file.
It automatically closes the file after finishing.
file becomes a file object that you can iterate through line by line.
💡 Python concept:
Using with open(...) is preferred over manual open() and close() — safer and cleaner.

6️⃣ Looping through lines
for line in file:
    stripped = line.strip()

Each iteration reads one line from the file.
.strip() removes all leading and trailing whitespace (spaces, tabs, newlines).

7️⃣ Filtering blank lines and comments
if not stripped or stripped.startswith("#"):
    continue

Here’s the logic:
not stripped → catches empty lines (after removing whitespace, nothing remains).
.startswith("#") → identifies comment lines, optionally preceded by spaces.
💡 Why not count docstrings as comments?
Because docstrings (triple-quoted strings inside functions/classes) are code, not comments — the spec explicitly says not to exclude them.

9️⃣ Handle missing files
except FileNotFoundError:
    sys.exit("File does not exist")

If the file doesn’t exist, Python raises a FileNotFoundError, which we catch gracefully.
💡 Python concept:
This is called exception handling.
You use try / except blocks to catch and handle predictable errors instead of letting your program crash.

🔟 The program entry point
if __name__ == "__main__":
    main()

When the file runs directly (python lines.py file.py), this block calls main().
But if it’s imported as a module (like import lines), it doesn’t execute main() automatically.


Python Concepts Learned
Concept	Explanation
sys.argv	Access command-line arguments
sys.exit()	Stop execution with a message
with open(...)	Safe file handling context manager
.strip()	Remove whitespace from both ends of a string
.startswith()	Check the prefix of a string
try / except	Error handling structure
FileNotFoundError	Specific error type for missing files
continue	Skip to the next loop iteration
if __name__ == "__main__":	Prevent code from running on import
raise vs sys.exit	Raise creates an exception; exit terminates program
"""


import sys
import os


def main():
    # check the input from command-line
    if len(sys.argv) != 2: # specify only one command line
        sys.exit("Two few or too many command-line arguments")

    filename = sys.argv[1]

    # file name must end by.py
    if not filename.endswith(".py"):
        sys.exit("Not a Python file")

    # Check if file exists
    if not os.path.isfile(filename):
        sys.exit("File does not exist")

    # Count lines of code
    try:
        count = count_lines(filename)
        print(count)
    except Exception as e:
        sys.exit(e)


def count_lines(filename):
    count = 0
    with open(filename, 'r') as file:
        for line in file:
            # strip removes leading/trailing whitespace
            stripped = line.strip()

            # algorithm: ignore blank lines and comments:
            if not stripped or stripped.startswith('#'):
                continue

            # count actual lines of code
            count += 1
    return count


if __name__ == '__main__':
    main()