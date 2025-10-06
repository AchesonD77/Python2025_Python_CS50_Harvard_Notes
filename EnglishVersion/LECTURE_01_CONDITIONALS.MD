# Lecture 1 — Conditionals

## Table of Contents
- [Conditionals](#conditionals)
- [if Statements](#if-statements)
- [Control Flow: `if`, `elif`, and `else`](#control-flow-elif-and-else)
- [`or`](#or)
- [`and`](#and)
- [Modulo](#modulo)
- [Creating Our Own Parity Function](#creating-our-own-parity-function)
- [Pythonic](#pythonic)
- [`match`](#match)
- [Summing Up](#summing-up)

---

## Conditionals

- **Conditionals** allow your program to *make decisions* based on certain conditions—choosing one path or another.
- Python provides comparison operators to ask mathematical questions:
  - `>` greater than
  - `<` less than
  - `>=` **greater than or equal to**
  - `<=` **less than or equal to**
  - `==` **equals** (note: single `=` assigns; double `==` compares)
  - `!=` **not equal to**
- A conditional compares a **left-hand term** to a **right-hand term** and evaluates to a Boolean (`True` or `False`).

---

## if Statements

- Create a file, e.g., `compare.py`, and start with:

```python
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
```
- Notice how your program takes the input of the user for both x and y, casting them as integers and saving them into their respective x and y variables. Then, the if statement compares x and y. If the condition of x < y is met, the print statement is executed.
- The `if` uses a Boolean expression (`x < y`). If it’s `True`, the indented block runs.

---

## Control Flow: `elif` and `else`

- Extend the program to cover more cases:

```python
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
if x > y:
    print("x is greater than y")
if x == y:
    print("x is equal to y")
```
- Notice how you are providing a series of if statements. First, the first if statement is evaluated. Then, the second if statement runs its evaluation. Finally, the last if statement runs its evaluation. This flow of decisions is called “control flow.”
  

- We can reduce unnecessary checks using **`elif`** (else-if) so only one branch runs:

```python
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y:
    print("x is less than y")
elif x > y:
    print("x is greater than y")
else:
    print("x is equal to y")
```
- While your computer may not notice a difference speed-wise between our first program and this revised program, consider how an online server running billions or trillions of these types of calculations each day could definitely be impacted by such a small coding decision.
  

- Note how **`else`** captures the “catch‑all” final case. This reduces complexity and improves performance.
- Notice how the relative complexity of this program has decreased through our revision.
---

## or

- `or` lets your program decide between **one or more alternatives**. Example:

```python
x = int(input("What's x? "))
y = int(input("What's y? "))

if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")
```
- Notice that the result of our program is the same, but the complexity is decreased. The efficiency of our code is increased.
  

- We can simplify even further by asking a single question with **`!=`**:

```python
x = int(input("What's x? "))
y = int(input("What's y? "))

if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")
```
- Notice how we removed the or entirely and simply asked, “Is x not equal to y?” We ask one and only one question. Very efficient!
  

- Reminder: **<mark>`==` compares values; `=` assigns</mark>**.
- Notice that the == operator evaluates if what is on the left and right are equal to one another. The use of double equal signs is very important. If you use only one equal sign, an error will likely be thrown by the interpreter.

```python
x = int(input("What's x? "))
y = int(input("What's y? "))

if x == y:
    print("x is equal to y")
else:
    print("x is not equal to y")
```

---

## and

- Similar to `or`, `and` can combine conditions. Let’s write a grading program (`grade.py`):

```python
score = int(input("Score: "))

if score >= 90 and score <= 100:
    print("Grade: A")
elif score >= 80 and score < 90:
    print("Grade: B")
elif score >= 70 and score < 80:
    print("Grade: C")
elif score >= 60 and score < 70:
    print("Grade: D")
else:
    print("Grade: F")
```
- Notice how Python allows you to chain together the operators and conditions in a way quite uncommon to other programming languages.
- Python lets us **chain comparisons** elegantly and readably:

```python
score = int(input("Score: "))

if 90 <= score <= 100:
    print("Grade: A")
elif 80 <= score < 90:
    print("Grade: B")
elif 70 <= score < 80:
    print("Grade: C")
elif 60 <= score < 70:
    print("Grade: D")
else:
    print("Grade: F")
```

- Fewer questions improves *readability* and maintainability.


- Still, we can further improve our program:
```python
score = int(input("Score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```
- Notice how the program is improved by asking fewer questions. This makes our program easier to read and far more maintainable in the future.
- You can learn more in Python’s documentation on control flow(https://docs.python.org/3/tutorial/controlflow.html).

---

## Modulo

- **Parity** asks whether a number is even or odd. The modulo operator **`%`** gives the remainder.
- The modulo % operator in programming allows one to see if two numbers divide evenly or divide and have a remainder.


- For example, 4 % 2 would result in zero, because it evenly divides. However, 3 % 2 does not divide evenly and would result in a number other than zero!
- Example (users can enter any integer ≥ 1):

```python
x = int(input("What's x? "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

## Creating Our Own Parity Function

- Let’s extract parity into a reusable function that returns a **bool**:

```python
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

main()
```
- Notice that our if statement is_even(x) works even though there is no operator there. This is because our function returns a bool (Boolean), True or False, back to the main function. The if statement simply evaluates whether or not is_even of x is true or false.
---

## Pythonic
- In the programming world, there are types of programming that are called “Pythonic” in nature. That is, there are ways to program that are sometimes only seen in Python programming. Consider the following revision to our program
  

- Python encourages concise, readable code. We can return the Boolean expression *directly*:

```python
def main():
    x = int(input("What's x? "))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return True if n % 2 == 0 else False
    # Or simply: return n % 2 == 0
```
- Notice that this return statement in our code is almost like a sentence in English. This is a unique way of coding only seen in Python.

- The return line reads almost like English—very **Pythonic**.
  
- Notice that the program will evaluate what is happening within the n % 2 == 0 as either True or False and simply return that to the main function.
---

## match

- Like `if`/`elif`/`else`, **`match`** (Python 3.10+) can conditionally run code based on exact values.


- Consider the following program:
```python
  name = input("What's your name? ")

  if name == "Harry":
      print("Gryffindor")
  elif name == "Hermione":
      print("Gryffindor")
  elif name == "Ron": 
      print("Gryffindor")
  elif name == "Draco":
      print("Slytherin")
  else:
      print("Who?")
```
- Notice the first three conditional statements print the same response.


- We can improve this code slightly with the use of the or keyword:
```python
  name = input("What's your name? ")

  if name == "Harry" or name == "Hermione" or name == "Ron": 
      print("Gryffindor")
  elif name == "Draco":
      print("Slytherin")
  else:
      print("Who?")
```
- Notice the number of elif statements has decreased, improving the readability of our code.


- Alternatively, we can use match statements to map names to houses. Consider the following code:

```python
  name = input("What's your name? ")

  match name: 
      case "Harry":
          print("Gryffindor")
      case "Hermione":
          print("Gryffindor")
      case "Ron": 
          print("Gryffindor")
      case "Draco":
          print("Slytherin")
      case _:
          print("Who?")
```
- Notice the use of the _ symbol in the last case. This will match with any input, resulting in similar behavior as an else statement.

- A match statement compares the value following the match keyword with each of the values following the case keywords. In the event a match is found, the respective indented code section is executed, and the program stops the matching.


```python
name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")
```

- The single vertical bar **`|`** acts like `or` inside a `case`.
- Notice, the use of the single vertical bar |. Much like the or keyword, this allows us to check for multiple values in the same case statement.
---

## Summing Up

You can now leverage conditionals to ask questions and take action:

- **Conditionals** and comparison operators  
- **`if`**, **`elif`**, **`else`** control flow  
- Logical operators: **`or`** and **`and`**  
- **Modulo** and parity checks  
- Writing **reusable functions** and *Pythonic* returns  
- Structural pattern matching with **`match`**
