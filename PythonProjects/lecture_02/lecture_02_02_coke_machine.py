"""
Task
We need to build coke.py:
Coke costs 50 cents.
Accepted coins: 25, 10, 5.
Ask the user repeatedly to insert a coin.
Show how much is still due after each valid coin.
If the user has paid ≥ 50, print the change owed.
Ignore invalid coins (don’t subtract from amount due).

Step 1: Tools We Need
1. input() and int()
We need to get coin input as integer:
coin = int(input("Insert coin: "))

2. Loop (while)
We must keep asking until enough money is inserted:
while amount_due > 0:
    ...

3. Conditions (if)
Check if the coin is valid (5, 10, 25).
If not, ignore it.

4. Output
Each time, show how much is still due.
When fully paid, show change.


Why while amount_due > 0?
We keep looping until the user has paid at least 50.

Why check if coin in insert_coins?
Only accept 5, 10, 25.
If the user enters 3, nothing happens, loop continues.

Why -amount_due for change?
If amount_due goes negative, that means the user overpaid.
Example:
Due = 10
User inserts 25
New amount_due = -15
Change owed = 15.
"""


def main():
    amount_due = 50
    insert_coins = [25, 10, 5]

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = int(input('Insert Coin:'))

        if coin in insert_coins:
            amount_due -= coin

    if amount_due < 0:
        print(f"Change Owed: {-amount_due}")
    else:
        print("Change Owed: 0")


main()



