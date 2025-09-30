# Creating Code with Python

- VS Code is a text editor. In addition to editing text, you can visually browse files and run text-based commands at a terminal.  

- In the terminal, you can execute `code hello.py` to start coding.  

- In the text editor above, you can type `print("hello, world")`. This is a famous canonical program that nearly all coders write during their learning process.  

- In the terminal window, you can execute commands. To run this program, you are going to need to move your cursor to the bottom of the screen, clicking in the terminal window. You can now type a second command in the terminal window. Next to the dollar sign, type `python hello.py` and press the enter key on your keyboard.  

- Recall that computers really only understand zeros and ones. Therefore, when you run `python hello.py`, Python will interpret the text that you created in `hello.py` and translate it into the zeros and ones that the computer can understand.  

- The result of running the `python hello.py` program is `hello, world`.  

- Congrats! You just created your first program.  

---

# Functions

- Functions are *verbs or actions* that the computer or computer language will already know how to perform.  
- In your `hello.py` program, the **`print` function** knows how to print to the terminal window.  
- The **`print` function takes arguments**. In this case, `"hello, world"` are the arguments that the `print` function takes.  

---

# Bugs

- Bugs are a *natural part of coding*. These are mistakes, problems for you to solve!  
  **Don’t get discouraged!** This is part of the process of becoming a great programmer.  

- Imagine that in our `hello.py` program we accidentally typed:  

  ```python
  print("hello, world"(forgetting the final ) 
  required by the print function).

- If you make this mistake, the interpreter will output **an error** in the terminal window!

- Error messages can often inform you of your mistakes and provide clues on how to fix them.
However, there will be many times when the interpreter is not this helpful.
  
---

# Improving Your First Python Program

- We can *personalize* your first Python program.  

- In our text editor in `hello.py` we can add another function. **`input`** is a function that takes a prompt as an argument. We can edit our code to say:

```python
input("What's your name? ")
print("hello, world")
```

- This edit alone, however, will not allow your program to output what your user inputs. For that, we will need to introduce you to **<mark>variables</mark>**.  

---

# Variables

- A *variable* is just a container for a value within your own program.  

- In your program, you can introduce your own variable by editing it to read:

```python
name = input("What's your name? ")
print("hello, world")
```

- Notice that this equal sign **`=`** in the middle of `name = input("What's your name? ")` has a **special role in programming**. This equal sign literally assigns what is on the right to what is on the left. Therefore, the value returned by `input("What's your name? ")` is assigned to **<mark>name</mark>**.  

- If you edit your code as follows, you will notice an *unexpected result*:

```python
name = input("What's your name? ")
print("hello, name")
```

- The program will return `hello, name` in the terminal window regardless of what the user types.  

- Further editing our code, you could type:

```python
name = input("What's your name? ")
print("hello,")
print(name)
```

- The result in the terminal window would be:

```text
What's your name? David
hello
David
```

- We are getting closer to the result we might intend! 🎉  
- You can learn more in Python’s documentation on **data types**: https://docs.python.org/3/library/stdtypes.html
---
# Strings and Parameters

- A string, known as a **`str`** in Python, is a *sequence of text*.
- Going back to our earlier code, we saw a visual side effect: the result appeared on multiple lines:

```python
# Ask the user for their name
name = input("What's your name? ")
print("hello,")
print(name)
```

- Functions take arguments that influence their behavior. Looking at the documentation for **`print`**, you’ll learn that it automatically includes the argument **`end='\n'`**. The `\n` indicates a newline.
- However, we can supply our own argument for **`end`** so that a new line is not created.
- Modify the code as follows:

```python
# Ask the user for their name
name = input("What's your name? ")
print("hello,", end="")
print(name)
```

- By providing **`end=""`** we overwrite the default newline so the output becomes `hello, David` (all on one line).
- **Parameters** are values that can be taken by a function. Learn more in Python’s docs on **`print`**: https://docs.python.org/3/library/functions.html#print

---

# A small problem with quotation marks

- Notice how adding quotation marks as part of your string is *challenging*.

- **<mark>`print("hello,"friend"")`</mark>** will not work, and the interpreter will throw an error.

- Generally, there are two approaches to fixing this.  
  1. Simply change the quotes to **single quotation marks**.  
  2. Another, more common approach is to escape the quotes with a backslash:

```python
print("hello, \"friend\"")
```

- The backslashes tell the interpreter that the following character should be treated as part of the string rather than ending it.  
- This way, the interpreter avoids an error.
---

# Formatting Strings

- The most elegant way to use strings here is an **f-string**:

```python
# Ask the user for their name
name = input("What's your name? ")
print(f"hello, {name}")
```

- Notice the **<mark>f</mark>** in `print(f"hello, {name}")`. The leading **f** tells Python to *format* the string and substitute expressions in `{…}`.

---

# More on Strings

- Never expect your user to cooperate perfectly—validate or clean their input.
- Strings provide methods to remove whitespace. Using **`strip()`** on **`name`** removes spaces on both sides:

```python
# Ask the user for their name
name = input("What's your name? ")

# Remove whitespace from the str
name = name.strip()

# Print the output
print(f"hello, {name}")
```

- We can also capitalize the first letter of each word using **`title()`**:

```python
# Ask the user for their name
name = input("What's your name? ")

# Remove whitespace and title-case
name = name.strip()
name = name.title()

print(f"hello, {name}")
```

- We can chain methods to be more efficient:

```python
# Ask the user for their name, strip spaces, and title-case
name = input("What's your name? ").strip().title()
print(f"hello, {name}")
```

- And we can go even further (equivalent result):

```python
name = input("What's your name? ").strip().title()
print(f"hello, {name}")
```

- Learn more about strings in Python’s docs on **`str`**: https://docs.python.org/3/library/stdtypes.html#text-sequence-type-str

---

# Integers (int)

- In Python, an integer is referred to as an **`int`**.
- In math we are familiar with the `+`, `-`, `*`, `/`, and `%` (modulo) operators.
- You can run Python code directly in the terminal with the REPL (`>>>`), but we’ll typically work in files.
- Create a new file via the terminal: `code calculator.py` (VS Code command on some setups), then write:

```python
x = 1
y = 2

z = x + y

print(z)
```

- Naturally, running `python calculator.py` prints `3`. We can make it interactive with **`input`**:

```python
x = input("What's x? ")
y = input("What's y? ")

z = x + y

print(z)
```

- The output becomes `12` because **`+`** concatenates strings，is incorrect. Because your input from your keyboard on your computer comes into the interpreter as text, it is treated as a string. We, therefore, need to convert this input from a string to an integer. We can do so as follows: Convert inputs to integers:

```python
x = input("What's x? ")
y = input("What's y? ")

z = int(x) + int(y)

print(z)
```

- Now it’s correct. This conversion with **`int(…)`** is called *casting*.
- We can improve the program further (nesting function calls—`input` then `int`):

```python
x = int(input("What's x? "))
y = int(input("What's y? "))

print(x + y)
```

- This shows we can run functions on functions. First `input`, then `int`.
- Learn more about **`int`**: https://docs.python.org/3/library/functions.html#int

---

# Readability Wins

- Regardless of approach, your code must be **readable**. Use comments to give yourself and others clues about what your code is doing.
- Prefer writing code in a way that maximizes clarity and maintainability.

---

# Float Basics

- A **float** is a real number with a decimal point, e.g., `0.52`.
- Update code to support floats:

```python
x = float(input("What's x? "))
y = float(input("What's y? "))

print(x + y)
```

- Now users can enter `1.2` and `3.4` to get `4.6`.

- To round to the nearest integer, see Python’s **`round`** docs (`round(number[, ndigits])`). Or do:

```python
# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))

# Create a rounded result
z = round(x + y)

print(z)
```

- To format large numbers with commas:
- What if we wanted to format the output of long numbers? For example, rather than seeing 1000, you may wish to see 1,000. You could modify your code as follows:
```python
x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x + y)

print(f"{z:,}")
```
- Though quite cryptic, that print(f"{z:,}") creates a scenario where the outputted z will include commas where the result could look like 1,000 or 2,500.

---

# More on Floats

- We will meet divide and see many decimal places:
- When inputting 2 as x and 3 as y, the result z is 0.6666666666, seemingly going on to infinity as we might expect.

```python
x = float(input("What's x? "))
y = float(input("What's y? "))

z = x / y

print(z)
```
- How can we round floating point values?
- Let’s imagine that we want to round this down. We could modify our code as follows:
- We can -> Round to two decimal places:

```python
x = float(input("What's x? "))
y = float(input("What's y? "))

z = round(x / y, 2)

print(z)
```
- As we might expect, this will round the result to the nearest two decimal points.
  
- Or format with an **f-string**:

```python
x = float(input("What's x? "))
y = float(input("What's y? "))

z = x / y

print(f"{z:.2f}")
```

- Learn more about **`float`**: https://docs.python.org/3/library/functions.html#float

---

# Def (Defining Functions)

- Wouldn’t it be nice to create our own functions?
- Bring back the final `hello.py` (using strip + title), then let’s refactor to a function from scratch:

```python
name = input("What's your name? ").strip().title()
hello()
print(name)
```

- Attempting to run this will error—`hello` isn’t defined yet. Define it:

```python
def hello():
    print("hello")

name = input("What's your name? ")
hello()
print(name)
```

- Everything inside `def hello():` is **indented**. Python uses indentation to define a function’s body.
- Improve the function to accept a parameter:

```python
# Create our own function
def hello(to):
    print("hello,", to)

# Output using our own function
name = input("What's your name? ")
hello(name)
```
- Here, in the first lines, you are creating your hello function. This time, however, you are telling the interpreter that this function takes a single parameter: a variable called to. Therefore, when you call hello(name) the computer passes name into the hello function as to. 
- This is how we pass values into functions. Very useful! Running python hello.py in the terminal window, you’ll see that the output is much closer to our ideal presented earlier in this lecture.


- Add a default parameter value:

```python
def hello(to="world"):
    print("hello,", to)

name = input("What's your name? ")
hello(name)

# Call without passing an argument
hello()
```
- Test out your code yourself. Notice how the first hello will behave as you might expect, and the second hello, which is not passed a value, will, by default, output hello, world.


- We can organize with a **`main`** function and call it:

```python
def main():
    # Output using our own function
    name = input("What's your name? ")
    hello(name)

    # Output without passing the expected arguments
    hello()

# Create our own function
def hello(to="world"):
    print("hello,", to)
```

- This alone won’t run anything because nothing calls `main`. Add a call:

```python
def main():
    name = input("What's your name? ")
    hello(name)
    hello()

def hello(to="world"):
    print("hello,", to)

main()
```

---

# Returning Values

- Sometimes we want a function to *return* a value, not just print.
- Back in `calculator.py`, rewrite:
- For example, rather than simply printing the calculation of x + y, you may want a function to return the value of this calculation back to another part of your program. This “passing back” of a value we call a return value.

```python
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n

main()
```

- Here, `x` is passed to **`square`**, and the calculation `x * x` is returned to `main`.

---

# Summing Up

Through this single lecture, you practiced:

- Creating your first programs in Python  
- Functions  
- Bugs  
- Variables  
- Comments  
- Pseudocode  
- Strings and <mark>parameters</mark>  
- Formatted strings (f-strings)  
- Integers and floats  
- Principles of <mark>readability</mark>  
- Creating your own functions  
- Returning values
