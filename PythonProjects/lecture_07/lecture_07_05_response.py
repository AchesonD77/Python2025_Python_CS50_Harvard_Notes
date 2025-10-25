"""
email validation and using external libraries in Python (instead of just regular expressions).

🎯 The Task
You must:
Prompt the user for an email address (input()).
Check if it’s syntactically valid (e.g., "user@example.com").
Print:
Valid if it’s a valid email format.
Invalid if not.
❌ You cannot use re (regular expressions).
✅ You must use validator-collection or validators library.

Why this works
The validators package (install via pip install validators) has a built-in email() function.
It does not raise exceptions — it simply returns:
True if the email format is valid.
a ValidationFailure object (which evaluates to False) if invalid.


"""


import validators

def main():
    email = input("What's your email address? ")
    if is_valid_email(email):
        print("Valid")
    else:
        print("Invalid")

# Why use is True instead of just returning the value?
# In Python, the is operator checks for object identity—it verifies if two variables point to the exact same object in memory.
#
# When the email is valid, validators.email(s) returns the built-in, singleton object True.
#
# The check (True) is True evaluates to True. (Correct)
#
# When the email is invalid, validators.email(s) returns the ValidationFailure object.
#
# The check (ValidationFailure object) is True evaluates to False because the object is not the literal True object. (Correct

def is_valid_email(s: str) -> bool:
    # validators.email returns True or ValidationFailure (falsy)
    return validators.email(s) is True
# return bool(validators.email(s))

if __name__ == "__main__":
    main()
