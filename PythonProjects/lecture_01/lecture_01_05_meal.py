'''
Task
In meal.py:
Prompt the user for a time in 24-hour format (HH:MM).
Convert it to hours as a float (e.g., "7:30" → 7.5).
Check ranges:
7:00 ≤ time ≤ 8:00 → breakfast time
12:00 ≤ time ≤ 13:00 → lunch time
18:00 ≤ time ≤ 19:00 → dinner time
If not in any range, output nothing.


Step 1: Tools We Need
1. .split(":")
Splits hours and minutes.
"7:30".split(":")  # ["7", "30"]

2. int() Conversion
Convert strings to integers.
int("7")   # 7
int("30")  # 30

3. Convert to float hours
hours + minutes / 60
Example:
7 + 30/60 = 7.5

4. if Ranges
if 7 <= t <= 8:
    print("breakfast time")

'''


def main():
    time = input("What time is it?")
    t = convert(time)

    if 7 <= t <= 8:
        print("breakfast time")
    elif 12 <= t <= 13:
        print("lunch time")
    elif 18 <= t <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    return hours + minutes / 60


if __name__ == "__main__":
    main()

