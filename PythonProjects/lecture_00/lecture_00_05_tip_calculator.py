# String Slicing / Removing Characters
# d[1:] → removes the first character.d[1:]
# p[:-1] → removes the last character.p[:-1]
#
# 1. Why d[1:]?
#
# Indexing in Python starts at 0.
#
# d[1:] means slice from index 1 until the end.
#
# So if d = "$50.00",
#
# d[0] = "$"
#
# d[1:] = "50.00"
#
# Why p[:-1]?
#
# p[:-1] means take everything except the last character.
#
# "15%"[:-1] = "15".
#
# float() Conversion
# Converts strings into floating-point numbers.


def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    return float(d[1:])


def percent_to_float(p):
    return float(p[:-1]) / 100
# If either operand is a float, the result is always a float.

main()