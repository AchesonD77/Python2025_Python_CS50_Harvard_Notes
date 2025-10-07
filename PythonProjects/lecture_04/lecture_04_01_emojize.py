"""
This one teaches how to use external libraries, string manipulation, and function calling in Python.

Prompts the user for a string in English.
Converts any emoji code (like :thumbs_up: or :smile:) to its actual emoji character (👍 😄).
Outputs the converted result.


Step 1: Required Library — emoji
Python has a built-in emoji package that does this conversion automatically.
You install it like this:
pip install emoji
Then you can use its main function:
emoji.emojize(":thumbs_up:")

Step 2: Complete Code


import emoji
This imports the external library we need.
input("Input: ")
This reads a line of text from the user

emoji.emojize(user_input, language="alias")
This function converts emoji codes (like :thumbs_up: or :heart:) into their actual emoji symbols (👍 ❤️).
The parameter language="alias" is important because:
it allows shorter alternative names like :thumbsup: instead of :thumbs_up:.
"""


import emoji


def main():
    user_input = input("Input: ")
    result = emoji.emojize(user_input, language="alias")
    print("Output:", result)


if __name__ == '__main__':
    main()