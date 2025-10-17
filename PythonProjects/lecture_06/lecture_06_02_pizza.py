"""
we learn to turn a CSV file (comma-separated values) into a visually formatted ASCII table using the Python library tabulate.
tests your understanding of file I/O, command-line arguments, CSV parsing, and third-party packages. 

import sys, import csv, from tabulate import tabulate
These are module imports, meaning you bring in external functionality.
sys → gives you access to command-line arguments and allows controlled program exits.
csv → the built-in Comma-Separated Values reader/writer module in Python.
tabulate → a third-party package that formats tables as readable text (ASCII art).
💡 Analogy:
import in Python is like “borrowing tools” from other toolkits — so you don’t reinvent features like argument parsing or table printing.

(a) Check the number of command-line arguments
if len(sys.argv) != 2:
    sys.exit("Too few or too many command-line arguments")

sys.argv is a list of everything typed after python pizza.py …
len(sys.argv) counts how many elements are in that list.
sys.exit() stops the program and prints the given message.

(b) Extract the filename
filename = sys.argv[1]

The first element [0] is always the script name (pizza.py),
so [1] is the actual user argument (like "sicilian.csv").

(c) Validate file type
if not filename.lower().endswith(".csv"):
    sys.exit("Not a CSV file")

.lower() makes it case-insensitive (so "SICILIAN.CSV" still works).
.endswith(".csv") checks if the filename ends with that extension.
If it’s not a CSV file, the program exits with a clear message — exactly what check50 expects.

3️⃣ File reading + error handling
try:
    rows = read_rows(filename)
except FileNotFoundError:
    sys.exit("File does not exist")
except Exception:
    sys.exit("Error reading file")

This block protects your program from crashing when:
The file doesn’t exist, or
There’s a weird encoding or CSV formatting issue.
💡 Concept: Exception Handling
When Python hits an unexpected error, it raises an exception.
try → run normally.
except → what to do if something goes wrong.
So your script will never display an ugly red “Traceback”. Instead, it exits neatly — as required by check50.

4️⃣ Printing the table
print(tabulate(rows, headers="keys", tablefmt="grid"))

This is the “pretty-print” step.
rows is a list of dictionaries (we’ll see soon how we created it).
headers="keys" tells tabulate to automatically use the dictionary keys (column names from the CSV header) as table headers.
tablefmt="grid" means you want an ASCII box-drawing style table.

5️⃣ The read_rows() helper function

This is where you read and process the CSV.
with open(filename, mode="r", encoding="utf-8-sig", newline="") as f:
    reader = csv.DictReader(f)
(a) with open(...)
This is a context manager — it opens a file safely and automatically closes it after the block finishes, even if there’s an error.

(b) Parameters explained
mode="r" → open the file for reading.
encoding="utf-8-sig" → ensures compatibility with BOM (Byte Order Mark) that some editors add. Without this, CS50’s files might crash on macOS/Windows.
newline="" → ensures csv module can correctly detect line endings across operating systems.

(c) csv.DictReader(f)
This reads the CSV and automatically converts each row into a dictionary, using the header row as the keys.

Example:
For this CSV:

Sicilian Pizza,Small,Large
Cheese,$25.50,$39.95
1 item,$27.50,$41.95

csv.DictReader produces:

[
  {'Sicilian Pizza': 'Cheese', 'Small': '$25.50', 'Large': '$39.95'},
  {'Sicilian Pizza': '1 item', 'Small': '$27.50', 'Large': '$41.95'}
]

(d) Convert to a list
rows = list(reader)
Because csv.DictReader returns an iterator (one-time use), you store it in a list for safe reuse.

csv.DictReader reads the first line as headers and produces each subsequent row as a dict like
{"Sicilian Pizza": "Cheese", "Small": "$25.50", "Large": "$39.95"}.


That avoids IndexError/header mistakes that cause the “Traceback …” you saw.
encoding="utf-8-sig" handles files that include a BOM (common on Windows/macOS editors). Without it, header parsing can fail and blow up later when tabulating.
newline='' follows the csv docs; it prevents subtle newline parsing issues across platforms.
tabulate(rows, headers="keys", tablefmt="grid") is the API designed for lists of dictionaries and produces the exact grid that check50 expects.
Clean exits with sys.exit("…") ensure no Python traceback ever reaches the output that check50 compares.
"""

import sys
import csv
from tabulate import tabulate


def main():
    # 1) exactly one argument
    if len(sys.argv) != 2:
        sys.exit("Too few or too many command-line arguments")

    filename = sys.argv[1]

    # 2) must be a .csv (case-insensitive)
    if not filename.lower().endswith(".csv"):
        sys.exit("Not a CSV file")

    # 3) read and render
    try:
        rows = read_rows(filename)
    except FileNotFoundError:
        sys.exit("File does not exist")
    except Exception:
        # any unexpected CSV/encoding issue → fail cleanly
        sys.exit("Error reading file")

    # 4) print as ASCII table in grid format
    # rows is a list of dicts; headers="keys" uses the CSV header row
    print(tabulate(rows, headers="keys", tablefmt="grid"))


def read_rows(filename: str):
    """
    Return a list of dictionaries from the CSV.
    Uses UTF-8-SIG to tolerate BOM headers in some editors.
    newline='' is recommended by csv module docs.
    """
    with open(filename, mode="r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        # DictReader automatically reads header row and maps each row to a dict
        rows = list(reader)  # materialize once; safe for reuse
        if not rows and reader.fieldnames is None:
            # truly malformed/empty CSV (no header)
            raise ValueError("Empty or malformed CSV")
        return rows


if __name__ == "__main__":
    main()