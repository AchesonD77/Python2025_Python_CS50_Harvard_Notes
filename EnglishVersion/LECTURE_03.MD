# Lecture 3 — Exceptions & Error Handling

## Table of Contents
- [Exceptions](#exceptions)
- [Runtime Errors](#runtime-errors)
- [try](#try)
- [else](#else)
- [Creating a Function to Get an Integer](#creating-a-function-to-get-an-integer)
- [pass](#pass)
- [Summing Up](#summing-up)

---

## Exceptions

- **Exceptions** are things that go wrong while your program is running.
- They are different from *syntax errors*, which the interpreter catches before the program starts.
- In your text editor, type `code hello.py` to create a new file. Type as follows (with the intentional error included):

```python
print("hello, world)
```

- Notice that we intentionally left out a quotation mark.
- Running `python hello.py` in the terminal produces a **SyntaxError**. Syntax errors generally mean you should double‑check that you typed your code correctly.
- You can learn more in Python’s documentation on <mark>Errors and Exceptions</mark> (https://docs.python.org/3/tutorial/errors.html).

---

## Runtime Errors

- **Runtime errors** refer to those created by unexpected behavior while your code runs. For example, you intended for a user to input a number, but they input a character instead.
- In your terminal window, run `code number.py`. Code as follows in your text editor:

```python
x = int(input("What's x? "))
print(f"x is {x}")
```

- By including the **f** (f‑string), we tell Python to interpolate the value of `x`.
- If we run this program and type `cat`, we’ll likely see:

```
ValueError: invalid literal for int() with base 10: 'cat'
```

- In other words, the <mark>int</mark> function cannot convert the text `'cat'` into a number.
- As programmers, we should be defensive to ensure that our users are entering what we expected.
- An effective strategy to fix this potential error would be to create “error handling” to ensure the user behaves as we intend.
- You can learn more in Python’s documentation of Errors and Exceptions (https://docs.python.org/3/tutorial/errors.html).

---

## try

- We can catch and handle user input errors before the program crashes by using **`try`** / **`except`**:

```python
try:
    x = int(input("What's x? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer")
```
- Notice how, running this code, inputting 50 will be accepted. However, typing in cat will produce an error visible to the user, instructing them why their input was not accepted.
  

- Let’s try to minimize the number of lines inside `try`. A *too minimal* version creates a new problem:

```python
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")

print(f"x is {x}")
```

- While this reduces code inside `try`, if the conversion fails, `x` is **never assigned**, so the last line raises a **NameError**: *`x` is not defined*.
- In short: when the `int(...)` conversion fails, the assignment to `x` never happens, so there is **no `x` to print**.

---

## else

- There’s a better pattern using **`try` / `except` / `else`**:

```python
try:
    x = int(input("What's x? "))
except ValueError:
    print("x is not an integer")
else:
    print(f"x is {x}")
```
- Notice that if no exception occurs, it will then run the block of code within else. 
- Running python number.py and supplying 50, you’ll notice that the result will be printed. Trying again, this time supplying cat, you’ll notice that the program now catches the error.
- Now the final print only runs if no exception occurs.
- We can also *politely reprompt* the user with a loop until they enter something acceptable:

```python
while True:
    try:
        x = int(input("What's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")
```
- Notice that while True will loop forever. If the user succeeds in supplying the correct input, we can break from the loop and then print the output. Now, a user that inputs something incorrectly will be asked for input again.


---

## Creating a Function to Get an Integer

- Many times we’ll want to get an integer from our user; let’s encapsulate that logic.

```python
def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("What's x?"))
        except ValueError:
            print("x is not an integer")
        else:
            break
    return x


main()
```

- Notice that we are manifesting many great properties. First, we have abstracted away the ability to get an integer. Now, this whole program boils down to the first three lines of the program.
  

- We can further improve this by returning directly from inside `try`:

```python
def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            x = int(input("What's x?"))
        except ValueError:
            print("x is not an integer")
        else:
            return x


main()
```
- Notice that return will not only break you out of a loop, but it will also return a value.


- Some might argue for an even shorter variant (same behavior, fewer lines):

```python
def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            print("x is not an integer")

main()
```
- Notice this does the same thing as the previous iteration of our code, simply with fewer lines.


---

## pass

- Sometimes you may not want to warn the user each time, but simply reprompt:

```python
def main():
    x = get_int()
    print(f"x is {x}")


def get_int():
    while True:
        try:
            return int(input("What's x? "))
        except ValueError:
            pass

main()
```
- Notice that our code will still function but will not repeatedly inform the user of their error. In some cases, you’ll want to be very clear to the user what error is being produced. Other times, you might decide that you simply want to ask them for input again.



- One more refinement: make the function accept a **prompt** string:

```python
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass

main()
```

- prompt is a parameter of the function get_int.
- When you call get_int("What's x? "), the string "What's x? " is passed into the function and stored in the variable prompt.


- prompt is a function parameter.

- When you call the function, you provide an argument (the actual string).

- That argument gets stored in the parameter variable (prompt) and used inside the function.


- You can learn more in Python’s documentation of <mark>pass</mark>. (https://docs.python.org/3/tutorial/controlflow.html#pass-statements)

---

## Summing Up

Errors are inevitable in your code. However, you can use what was learned today to help prevent these errors. In this lecture, you learned about…

- **Exceptions**
- **ValueError** and other *runtime errors*
- **<mark>try</mark>**
- **<mark>else</mark>**
- **<mark>pass</mark>**
