"""
Task Recap
In nutrition.py:
Ask the user for a fruit (case-insensitive).
Look up the number of calories from the FDA’s list.
Print the calories if it’s in the list.
If not, print nothing.

Step 1: Use a Dictionary
We use a Python dictionary (dict) to store fruit → calories mapping:
fruits = {
    "apple": 130,
    "banana": 110,
    "strawberries": 50,
    "watermelon": 80,
    ...
}

Step 2: Normalize Input
To handle both Apple and apple the same way, convert input to lowercase:
fruit = input("Item: ").lower()

Step 3: Look Up Calories
Check if the fruit is in the dictionary. If yes, print the calories:
if fruit in fruits:
    print("Calories:", fruits[fruit])


Why .lower()?
Ensures case-insensitivity. "Apple", "APPLE", "apple" → all become "apple".

Why a dictionary instead of many if-statements?
Cleaner, faster lookups.
Easy to maintain if the list grows.

Why if fruit in fruits:?
Prevents KeyError.
If fruit isn’t in the list, nothing happens.
"""


def main():
    fruits = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwifruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "peach": 60,
        "pear": 100,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80
    }

    fruit = input("Item: ").lower()
    if fruit in fruits:
        print("Calories: ", fruits[fruit])


if __name__ == '__main__':
    main()