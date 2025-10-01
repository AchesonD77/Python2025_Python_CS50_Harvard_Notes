'''
Task
In camel.py, write a program that:
Takes a variable name written in camelCase (like firstName).
Converts it into snake_case (like first_name).

1. input()
Ask the user

2. Loop through string characters
We need to detect uppercase letters:
for c in camel:
    if c.isupper():
        # Do something

3. .isupper()
Checks if a character is uppercase:
"A".isupper()  # True
"a".isupper()  # False

4. str.lower()
Converts to lowercase:
"A".lower()  # "a"

5. Building the new string
Start with an empty string and add characters one by one:
snake = ""


'''


def main():
    camel = input("camelCase: ")
    snake = ''

    for i in camel:
        if i.isupper():
            snake += "_" + i.lower()
        else:
            snake += i

    print("snak_case:", snake)

main()
