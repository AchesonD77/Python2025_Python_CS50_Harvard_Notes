"""
CS50P Problem Set 7: “NUMB3RS”, which asks you to write a Python program that validates whether a given string is a valid IPv4 address.

An IPv4 address looks like:
#.#.#.#   →  for example: 192.168.0.1
Each number (called an octet) must:
be between 0 and 255, inclusive
contain only digits (no letters, no spaces, no negatives)

Step 1 — Plan the Logic
We need to write a function:
def validate(ip):
that returns True or False.
We can solve this problem using a regular expression (re module).
Why use Regular Expressions (regex)?
Regex helps match patterns in strings — perfect for structured formats like IP addresses.


① import re
We use the re (regular expression) library for pattern matching.
② Regular Expression r'^([0-9]{1,3}\.){3}[0-9]{1,3}$'
Let’s decode it:
Part	Meaning
^	Start of string
([0-9]{1,3}\.){3}	Three groups of 1–3 digits followed by a dot
[0-9]{1,3}	Last group of 1–3 digits (no trailing dot)
$	End of string
So, it matches patterns like "192.168.0.1" or "10.0.0.255" — but not "192.168.0." or "10.0.0.999" yet (we check range separately).

③ re.match(pattern, ip)
This returns a match object if the string fits the pattern; otherwise, None.

It rejects any part that:
has more than one digit (len(part) > 1)
and starts with a 0 → e.g. "01", "001", "010".
Thus:
✅ "0.0.0.0" → valid
❌ "000.001.010.100" → invalid

④ ip.split(".")
We separate the IP by dots into a list:
"192.168.0.1" → ['192', '168', '0', '1']

⑤ Range Check
Each octet must be 0 ≤ value ≤ 255.
If any octet fails, return False.
"""


import re
import sys


import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Basic regex pattern: ensure four groups of digits separated by dots
    pattern = r"^([0-9]{1,3}\.){3}[0-9]{1,3}$"
    if not re.match(pattern, ip):
        return False

    # Split into octets and check each
    parts = ip.split(".")
    for part in parts:
        # Rule A: each part must be digits only (already guaranteed by regex)
        # Rule B: numerical range check
        if int(part) < 0 or int(part) > 255:
            return False
        # Rule C: reject leading zeros (e.g., "01", "001", "010")
        if len(part) > 1 and part[0] == "0":
            return False

    return True


if __name__ == "__main__":
    main()


