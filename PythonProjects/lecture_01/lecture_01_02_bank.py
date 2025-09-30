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

def bank_gretting():
    gretting = input("Greeting: ").strip().lower()

    if gretting.startswith("hello"):
        print("$0")
    elif gretting.startswith("h"):
        print("$20")
    else:
        print("$100")


bank_gretting()


