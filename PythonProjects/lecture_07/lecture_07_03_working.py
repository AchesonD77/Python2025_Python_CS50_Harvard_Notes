"""
write a function convert(s) that takes a 12-hour time range like:
9:00 AM to 5:00 PM
9 AM to 5 PM
9:00 AM to 5 PM
9 AM to 5:00 PM

…and returns the 24-hour version:
09:00 to 17:00
If the input is malformed or a time is impossible (e.g., 13:00 PM, 12:60 AM), raise ValueError.


r'^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$'
^ … $ → entire line match (no extra text)

(\d{1,2}) → one or two digits for hour

(?::(\d{2}))? → optional colon and two digits (minutes)

(AM|PM) → exactly AM or PM (capitalized)

Spaces are required where the problem specifies (e.g., "9 AM" not "9AM")

" to " required literally (test checks for that exact substring)

"""

import re


def main():
    print(convert(input("Hours: ")))


def convert(s: str) -> str:
    # Regex that accepts:
    #   - hour 1–2 digits
    #   - optional :MM where MM is 00–59
    #   - AM/PM (capitalized)
    #   - flexible spaces around tokens
    pattern = r'^(\d{1,2})(?::(\d{2}))? (AM|PM) to (\d{1,2})(?::(\d{2}))? (AM|PM)$'

    m = re.match(pattern, s.strip())
    if not m:
        raise ValueError('Invalid format')

    h1, m1, AP1, h2, m2, AP2 = m.groups()

    h1 = int(h1)
    h2 = int(h2)

    m1 = int(m1) if m1 is not None else 0
    m2 = int(m2) if m2 is not None else 0


    if not (1 <= h1<= 12) or not (1 <= h2 <= 12):
        raise ValueError("Hour out of range")
    if not (0 <= m1 < 60) or not (0 <= m2 < 60):
        raise ValueError("Minute out of range")

    # convert
    H1, M1 = to_24(h1, m1, AP1)
    H2, M2 = to_24(h2, m2, AP2)

    return f"{H1:02d}:{M1:02d} to {H2:02d}:{M2:02d}"


def to_24(hour: int, minute: int, am_pm: str) -> tuple[int, int]:
    if am_pm == "AM":
        hour = 0 if hour == 12 else hour
    else:
        hour = 12 if hour == 12 else hour + 12
    return hour, minute


if __name__ == '__main__':
    main()

