'''
1. input() + .strip()
Remove extra spaces from start/end.
2. .lower()
Makes everything lowercase → easy comparison.
3. .startswith()
It’s a string method in Python that checks if a string begins with a certain substring.
Returns a boolean (True or False).
It doesn’t change the string; it just checks.


Why .startswith()?
More robust than slicing (greeting[:5] == "hello").
It works for all string lengths and avoids errors if greeting is shorter.


You can check for more than one option using a tuple:

greeting = "hey"
print(greeting.startswith(("hi", "hey", "hello")))  # True

'''


def main():
    greeting = input("Greeting: ")
    print(f"${value(greeting)}")


def value(greeting):
    greeting = greeting.strip().lower()

    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()