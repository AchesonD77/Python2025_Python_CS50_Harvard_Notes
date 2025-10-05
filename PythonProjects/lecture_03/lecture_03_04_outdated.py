"""
train your string manipulation, list indexing, error handling, and date formatting skills

Problem Goal
We must write a program called outdated.py that:
Prompts the user for a date.
Accepts two formats:
MM/DD/YYYY → e.g. 9/8/1636
Month D, YYYY → e.g. September 8, 1636
Converts it into ISO 8601 format:
YYYY-MM-DD
Keeps prompting until the user enters a valid date.


Step 1: Think About the Data Structures
We’ll use a list to store the month names:
Why a list?
✅ Lists preserve order — January = index 0, February = index 1, etc.
✅ We can find a month’s number easily using .index().

Step 2: Plan Input Parsing
There are two main formats to recognize:
Format	Example	How to Split
Numeric	9/8/1636	Use .split("/")
Textual	September 8, 1636	Use .split(" ") and strip commas
We can use:
str.split() to break input into parts.
str.strip() to remove spaces or commas.
int() to convert to numbers.
try/except to handle invalid input gracefully.


while True:
Keeps looping until valid input is entered.
We exit (break) once we successfully print the formatted date.

input("Date: ").strip()
Prompts for a string and removes extra spaces.

if "/" in date:
Detects whether the input is numeric format (MM/DD/YYYY)
and splits it using .split("/").
month, day, year = date.split("/")
Python automatically unpacks the three parts into three variables.

else:
Handles text format like September 8, 1636.
We remove the comma using .replace(",", "")
and split by space.
.index() finds the position of "September" in the list (which is 8th → index 8 → +1 = 9).

Validation
if not (1 <= month <= 12 and 1 <= day <= 31):
    raise ValueError
This ensures we only accept valid month/day ranges.
We don’t check exact month lengths (like February 30) — CS50 says no need.

Print formatted result
:04 → 4 digits, padded with zeros (e.g., 1636)
:02 → 2 digits (e.g., 09, 08)

except (ValueError, IndexError):

Catches both:
Wrong number formats (e.g., “13/99/2000”)
Invalid month names (“Smarch” 😂)
Then it continues the loop and reprompts.

Knowledge Recap
Concept	What It Does	Example
str.split()	Splits a string into parts	"9/8/1636".split("/") → ["9","8","1636"]
str.strip()	Removes spaces around text	" hello ".strip() → "hello"
str.replace()	Replaces one substring with another	"8, 1636".replace(",", "") → "8 1636"
list.index()	Finds the position of an element	months.index("September") → 8
f"{var:02}"	Formats number to 2 digits	f"{9:02}" → "09"
try / except	Prevents crash on bad input	except ValueError:
"""


def main():
    months = [ "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"]

    while True:
        try:
            date = input("Date: ".strip())

            # case 1: m/d/year
            if '/' in date:
                month, day, year = date.split('/')
                month = int(month)
                day = int(day)
                year = int(year)

            # case 2: September 8, 2000
            elif ',' in date:
                month_str, day, year = date.replace(",", "").split(" ")
                month = months.index(month_str) + 1
                day = int(day)
                year = int(year)

            else:
                raise  ValueError
            #
            if not (1 <= month <= 12 and 1 <= day <= 31):
                raise ValueError

            print(f"{year:04}-{month:02}-{day:02}")
            break

        except (ValueError, IndexError):
            continue


if __name__ == '__main__':
    main()

"""
Summary Table
Keyword	Function	Typical Use
raise	Manually throw an error	When something invalid happens
except	Catch and handle raised (or automatic) errors	To prevent crashing
try	Marks code that might cause an error	Paired with except
Together	try runs → raise creates → except catches	Controlled error management
"""