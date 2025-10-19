"""
“Scourgify” problem, where you’ll “clean up” a messy CSV file.

In this exercise, you’ll learn:
How to read and write CSV files properly,
How to split strings intelligently,
How to use Python’s csv.DictReader and csv.DictWriter,
And how to handle command-line arguments safely.

sys → for command-line arguments and clean program exits.
csv → the built-in library that handles reading/writing CSV files easily.

Step 1: Validate arguments
The user must provide two arguments:
1️⃣ the input CSV file (before.csv),
2️⃣ the output CSV file (after.csv).
If the user gives fewer or more, the program exits gracefully with an error.

Step 2: Assign filenames
Now the program knows what file to read and where to save the cleaned version.

Step 3: Try reading the file
If the input file doesn’t exist, Python raises a FileNotFoundError.
We catch that and exit cleanly (no ugly “Traceback”).
✅ Good software never crashes unexpectedly — it fails gracefully.

Step 4: Write the output file
This hands off the clean data to another function to save it — keeping our code modular and organized.

Function: read_students(filename)
This is where the “Scourgify magic” happens ✨ — cleaning up the messy data.

Step 1: Open the file safely
with open(...) automatically closes the file — even if an error occurs.
newline="" avoids extra blank lines on Windows.
encoding="utf-8" ensures all characters are read properly.
csv.DictReader reads each line into a dictionary, using the first line (name,house) as keys.

Step 2: Clean and split the name
Here’s what happens:
.strip('"') removes double quotes from around the name.
→ "Abbott, Hannah" → Abbott, Hannah
.split(",") splits the name into two parts:
→ ["Abbott", " Hannah"]
[part.strip() for part in ...] removes extra spaces around each part.
→ ["Abbott", "Hannah"]

So we get:
last = "Abbott"
first = "Hannah"

Step 3: Create a clean dictionary
Now we store each student as a dictionary.
After the loop, students looks like this:
[
  {"first": "Hannah", "last": "Abbott", "house": "Hufflepuff"},
  {"first": "Katie", "last": "Bell", "house": "Gryffindor"},
  {"first": "Susan", "last": "Bones", "house": "Hufflepuff"},
  ...
]

Function: write_students(students, filename)
This writes the cleaned data back to a new file.

Explanation:
csv.DictWriter lets you write dictionaries directly as CSV rows.
fieldnames defines the order of columns.
writer.writeheader() writes the header line:
first,last,house
writer.writerow(student) writes each student’s data on a new line.

The main guard
if __name__ == "__main__":
    main()
This ensures the script runs only when executed directly —
not when imported into another file.

"""

""" verision 1
import sys
import csv


def main():
    # check command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Too few or too many command-line arguments")

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # read the input file
    try:
        students = read_students(input_file)
    except FileNotFoundError:
        sys.exit(f"Could not read {input_file}")

    # write the file and output
    write_students(students, output_file)


def read_students(filename):
    students = []
    with open(filename, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            full_name = row['name'].strip('"')
            last, first = [part.strip() for part in full_name.split(',')]
            house = row['house'].strip()
            students.append({
                "first" : first,
                "last" : last,
                "house" : house
            })
    return students


def write_students(students, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['first', 'last', 'house'])
        writer.writeheader()
        for student in students:
            writer.writerow(student)


if __name__ == '__main__':
    main()
 """

""" verision 2 """
# scourgify.py
import sys
import csv

def main():
    # must be exactly 2 args: input.csv output.csv
    if len(sys.argv) != 3:
        sys.exit("Too few or too many command-line arguments")

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    try:
        with open(input_path, "r", newline="") as src:
            reader = csv.DictReader(src)              # expects columns: name, house
            with open(output_path, "w", newline="") as dst:
                writer = csv.DictWriter(dst, fieldnames=["first", "last", "house"])
                writer.writeheader()
                for row in reader:
                    # row["name"] like: "Potter, Harry"
                    # split on comma+space to avoid stray spaces
                    last, first = row["name"].split(", ")
                    writer.writerow({"first": first, "last": last, "house": row["house"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {input_path}")


if __name__ == "__main__":
    main()