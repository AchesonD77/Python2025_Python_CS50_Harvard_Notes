"""
count how many times “um” appears as a stand-alone word, case-insensitive,
not as part of another word like yummy or album. Regex is perfect here.

Why this works (professor mode 🎓)
\b word boundary matches the edge between word characters ([A-Za-z0-9_]) and non-word characters (space, punctuation, start/end of string).
So it matches um,, um., (um) and doesn’t match yummy, album, aluminum.
re.findall returns all non-overlapping matches; len(...) is the count.
re.IGNORECASE makes it match any capitalization of “um”.
"""


import re


def main():
    print(count(input("Text: ")))


def count(s: str) -> int:
    # \b = word boundary    only focus on the word um
    # IGNORECASE → case-insensitive matching
    hits = re.findall(r'\bum\b', s, flags=re.IGNORECASE)
    return len(hits)


if __name__ == '__main__':
    main()
