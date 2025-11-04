# Lecture 9 — *Et Cetera* (Python Odds & Ends)

> Keep the same style and structure as previous lectures. Key ideas are **bold**, clarifications are *italic*, and high‑value tips are <mark>highlighted</mark>.

## Table of Contents
- [Et Cetera](#et-cetera)
- [set](#set)
- [Global Variables](#global-variables)
- [Constants](#constants)
- [Type Hints](#type-hints)
- [Docstrings](#docstrings)
- [argparse](#argparse)
- [Unpacking](#unpacking)
- [args and kwargs](#args-and-kwargs)
- [map](#map)
- [List Comprehensions](#list-comprehensions)
- [filter](#filter)
- [Dictionary Comprehensions](#dictionary-comprehensions)
- [enumerate](#enumerate)
- [Generators and Iterators](#generators-and-iterators)
- [Congratulations!](#congratulations)
- [This was CS50!](#this-was-cs50)

---

## Et Cetera

- Across many past lessons, we’ve covered so much related to Python.
- In this lesson, we focus on the “*et cetera*” items not previously discussed—literally “and the rest.”
- In the Python docs, this is effectively “the rest” of the features.

---

## set

- In math, a **set** is a collection of unique elements (no duplicates). In Python, `set` works similarly.

```py
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

houses = []
for student in students:
    if student["house"] not in houses:
        houses.append(student["house"])

for house in sorted(houses):
    print(house)
```
- Notice how we have a list of dictionaries, each being a student. An empty list called houses is created. We iterate through each student in students. If a student’s house is not in houses, we append to our list of houses.
  

- It turns out we can use the built-in set features to eliminate duplicates.
- Using a `set` eliminates duplicates automatically:

```py
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

houses = set()
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)
```
- You can learn more in Python’s documentation of set. https://docs.python.org/3/library/stdtypes.html#set

<mark>No need to manually check for duplicates—`set` handles it.</mark>

---

## Global Variables

- Some languages have **global variables** accessible from any function. Python permits this, but use **sparingly**.

```py
balance = 0

def main():
    print("Balance:", balance)

if __name__ == "__main__":
    main()
```
- Notice how we create a global variable called balance, outside of any function.
  

- Adding functions shows a common pitfall (unbound local):

```py
balance = 0

def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)

def deposit(n):
    balance += n         # UnboundLocalError

def withdraw(n):
    balance -= n

if __name__ == "__main__":
    main()
```
- Notice how we now add the functionality to add and withdraw funds to and from balance. However, executing this code, we are presented with an error! We see an error called UnboundLocalError. You might be able to guess that, at least in the way we’ve currently coded balance and our deposit and withdraw functions, we can’t reassign it a new value inside a function.


- Fix by declaring the name as **global** *inside* the functions that mutate it:

```py
balance = 0

def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)

def deposit(n):
    global balance
    balance += n

def withdraw(n):
    global balance
    balance -= n

if __name__ == "__main__":
    main()
```
- Notice how the global keyword tells each function that balance does not refer to a local variable: instead, it refers to the global variable we originally placed at the top of our code. Now, our code functions!
  

- <mark>Better pattern:</mark> encapsulate state in a **class**.

```py
class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n

def main():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)

if __name__ == "__main__":
    main()
```
- Notice how we use account = Account() to create an account. Classes allow us to solve this issue of needing a global variable more cleanly because these instance variables are accessible to all the methods of this class utilizing self


- Generally speaking, global variables should be used quite sparingly, if at all!


---

## Constants

- Some languages support **constants**. Python doesn’t enforce them, but by **convention** we write them in ALL_CAPS and *don’t change them*.

```py
MEOWS = 3
for _ in range(MEOWS):
    print("meow")
```
- Notice MEOWS is our constant in this case. Constants are typically denoted by capital variable names and are placed at the top of our code. Though this looks like a constant, in reality, Python actually has no mechanism to prevent us from changing that value within our code! Instead, you’re on the honor system: if a variable name is written in all caps, just don’t change it!
  

- One can create a class “constant”, now in quotes because we know Python doesn’t quite support “constants”. In the text editor window, code as follows:

- A pseudo‑constant on a class:

```py
class Cat:
    MEOWS = 3
    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")

cat = Cat()
cat.meow()
```
- Because MEOWS is defined outside of any particular class method, all of them have access to that value via Cat.MEOWS.


---

## Type Hints

- In other programming languages, one expresses explicitly what variable type you want to use.
- As we saw earlier in the course, Python does not require the explicit declaration of types.
- Nevertheless, it’s good practice need to ensure all of your variables are of the right type.  


- Python is dynamically typed, but **type hints** help tools (and you!) catch errors early. Install `mypy` via:

```bash
pip install mypy
```

- Without hints we might do this:

```py
def meow(n):
    for _ in range(n):
        print("meow")

number = input("Number: ")   # str, not int
meow(number)                 # likely error at runtime
```
- You may already see that number = input("Number: )" returns a string, not an int. But meow will likely want an int!
  

- A type hint can be added to give Python a hint of what type of variable meow should expect. In the text editor window, code as follows:
- Add hints and convert inputs:

```py
def meow(n: int) -> None:
    for _ in range(n):
        print("meow")

number: int = int(input("Number: "))
meow(number)
```
- Notice how number is now provided a type hint.
- Again, executing mypy meows.py in the terminal window provides much more specific feedback to you, the programmer.
- Notice how running mypy now produces no errors because we cast our input to an integer.


- Let’s introduce a new error by assuming that meow will return to us a string, or str. In the text editor window, code as follows:
- Return values can be annotated too:

```python
def meow(n: int):
    for _ in range(n):
        print("meow")


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows)
```
- no return: Notice how the meow function has only a side effect. Because we only attempt to print “meow”, not return a value, an error is thrown when we try to store the return value of meow in meows.


- Notice how the notation -> None tells mypy that there is no return value.

```py
def meow(n: int) -> str:
    return "meow\n" * n

number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")
```
- Notice how we store in meows multiple strs. Running mypy produces no errors.

- You can learn more in Python’s documentation of Type Hints. https://docs.python.org/3/library/typing.html

- You can learn more about mypy through the program’s own documentation. https://mypy.readthedocs.io/

<mark>Run `mypy` to get static feedback.</mark>

---

## Docstrings

- A standard way of commenting your function’s purpose is to use a docstring.
  
- You can use docstrings to standardize how you document the features of a function. 
- A **docstring** documents a function/class/module. Triple quotes below the definition:

```py
def meow(n: int) -> str:
    """Meow n times.

    :param n: Number of times to meow
    :type n: int
    :raises TypeError: If n is not an int
    :return: A string of n meows, one per line
    :rtype: str
    """
    return "meow\n" * n
```
- Notice how multiple docstring arguments are included. For example, it describes the parameters taken by the function and what is returned by the function.
  

- Tools like **Sphinx** can render docstrings into HTML/PDF. <mark>Good docs are part of good code.</mark>
- You can learn more in Python’s documentation of docstrings. https://peps.python.org/pep-0257/
---

## argparse

- Parse command‑line arguments robustly with **argparse**.


- Suppose we want to use command-line arguments in our program. 
```python
import sys

if len(sys.argv) == 1:
    print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n":
    n = int(sys.argv[2])
    for _ in range(n):
        print("meow")
else:
    print("usage: meows.py [-n NUMBER]")
```
- Notice how sys is imported, from which we get access to sys.argv, an array of command-line arguments given to our program when run. We can use several if statements to check whether the user has run our program properly.
- Let’s assume that this program will be getting much more complicated. How could we check all the arguments that could be inserted by the user? We might give up if we have more than a few command-line arguments!


- Luckily, argparse is a library that handles all the parsing of complicated strings of command-line arguments. 



```py
import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("meow")
```
- Notice how argparse is imported instead of sys. An object called parser is created from an ArgumentParser class. That class’s add_argument method is used to tell argparse what arguments we should expect from the user when they run our program. Finally, running the parser’s parse_args method ensures that all of the arguments have been included properly by the user.

- Notice how the user is provided some documentation. Specifically, a help argument is provided. Now, if the user executes python meows.py --help or -h, the user will be presented with some clues about how to use this program.

- Notice how not only is help documentation included, but you can provide a default value when no arguments are provided by the user.


- You can learn more in Python’s documentation of argparse. https://docs.python.org/3/library/argparse.html
---

## Unpacking

- Would it not be nice to be able to split a single variable into two variables?

```py
first, _ = input("What's your name? ").split(" ")
print(f"hello, {first}")
```
- Notice how this program tries to get a user’s first name by naively splitting on a single space.


- What if we wanted to store our coins in a list?
```python
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = [100, 50, 25]

print(total(*coins), "Knuts")
``` 
- Suppose that we could pass in the names of the currency in any order?
```python
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


print(total(galleons=100, sickles=50, knuts=25), "Knuts")
```
- Notice how this still calculates correctly.


- When you start talking about “names” and “values,” dictionaries might start coming to mind! You can implement this as a dictionary. In the text editor window, code as follows:
```python
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts")
```
- Since the total function expects three arguments, we cannot pass in a dictionary. We can use unpacking to help with this. In the text editor window, code as follows:
```python
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


coins = {"galleons": 100, "sickles": 50, "knuts": 25}

print(total(**coins), "Knuts")
```  

- Notice how ** allows you to unpack a dictionary. When unpacking a dictionary, it provides both the keys and values.
  


- Notice how a * unpacks the sequence of the list of coins and passes in each of its individual elements to total.


```py
def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

print(total(*[100, 50, 25]), "Knuts")
print(total(**{"galleons":100, "sickles":50, "knuts":25}), "Knuts")
```


---

## args and kwargs

- `*args` collects positional arguments; `**kwargs` collects keyword arguments.


- args are positional arguments, such as those we provide to print like print("Hello", "World").
- kwargs are named arguments, or “keyword arguments”, such as those we provide to print like print(end="").


```py
def f(*args, **kwargs):
    print("Positional:", args)
    print("Named:", kwargs)

f(100, 50, 25, galleons=100, sickles=50, knuts=25)
```
- As we see in the prototype for the print function above, we can tell our function to expect a presently unknown number positional arguments. We can also tell it to expect a presently unknown number of keyword arguments.
- Notice how the named values are provided in the form of a dictionary.
- You can learn more in Python’s documentation of print.  https://docs.python.org/3/library/functions.html#print
---

## map

- Functional style: apply a function to each element.

- Wouldn’t it be nice to yell a list of unlimited words?

```py
def main():
    yell(["This", "is", "CS50"])


def yell(words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)


if __name__ == "__main__":
    main()
```
- Notice we accumulate the uppercase words, iterating over each of the words and “uppercasing” them. The uppercase list is printed utilizing the * to unpack it.


- Removing the brackets, we can pass the words in as arguments. 
```python
def main():
    yell("This", "is", "CS50")


def yell(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)


if __name__ == "__main__":
    main()
```
- Notice how *words allows for many arguments to be taken by the function.


- map allows you to map a function to a sequence of values. In practice, we can code as follows:
```py
def main():
    yell("This", "is", "CS50")


def yell(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)


if __name__ == "__main__":
    main()
```
- Notice how map takes two arguments. First, it takes a function we want applied to every element of a list. Second, it takes that list itself, to which we’ll apply the aforementioned function. Hence, all words in words will be handed to the str.upper function and returned to uppercased.

- You can learn more in Python’s documentation of map. https://docs.python.org/3/library/functions.html#map
__
---

## List Comprehensions

- List comprehensions allow you to create a list on the fly in one elegant one-liner.
- Create lists in one line:

```py
def main():
    yell("This", "is", "CS50")


def yell(*words):
    uppercased = [arg.upper() for arg in words]
    print(*uppercased)


if __name__ == "__main__":
    main()

```
- Notice how instead of using map, we write a Python expression within square brackets. For each argument, .upper is applied to it.



- Filter while building:
- another program

```python
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

gryffindors = []
for student in students:
    if student["house"] == "Gryffindor":
        gryffindors.append(student["name"])

for gryffindor in sorted(gryffindors):
    print(gryffindor)
```
- Notice we have a conditional while we’re creating our list. If the student’s house is Gryffindor, we append the student to the list of names. Finally, we print all the names.


- More elegantly, we can simplify this code with a list comprehension as follows:

```py
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]
gryffindors = [student["name"] for student in students if student["house"] == "Gryffindor"]
for g in sorted(gryffindors):
    print(g)
```
- Notice how the list comprehension is on a single line!

---

## filter

- Return a subset based on a predicate:

```py
students = [
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
]

def is_gryffindor(s): return s["house"] == "Gryffindor"

gryffindors = filter(is_gryffindor, students)
for g in sorted(gryffindors, key=lambda s: s["name"]):
    print(g["name"])

# Lambda version
gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)
```

---

## Dictionary Comprehensions

```py
students = ["Hermione", "Harry", "Ron"]
gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]
print(gryffindors)

# Or a mapping
gryffindors = {student: "Gryffindor" for student in students}
print(gryffindors)
```

---

## enumerate

- Iterate with an index:

```py
students = ["Hermione", "Harry", "Ron"]

for i, student in enumerate(students, start=1):
    print(i, student)
```

---

## Generators and Iterators

- Programs can run out of memory if building huge lists. A **generator** <mark>yields</mark> values one by one.

Basic counting sheep:

```py
n = int(input("what's n? "))
for i in range(n):
    print("🐑" * i)
```

Refactor with functions:

```py
def main():
    n = int(input("what's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    flock = []
    for i in range(n):
        flock.append("🐑" * i)
    return flock
```

Use a **generator** to stream results:

```py
def main():
    n = int(input("what's n? "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield "🐑" * i   # yields one at a time
```

<mark>Benefit:</mark> constant memory, even for huge `n`. See Python docs on **generators** and **iterators**.

---

## Congratulations!

You now have a stronger toolbox for programming:
1. Functions and variables
2. Conditionals
3. Loops
4. Exceptions
5. Libraries
6. Unit tests
7. File I/O
8. Regular expressions
9. Object‑oriented programming
10. And today: many more tools (sets, types, parsing, generators, …)

---

## This was CS50!

Build a spirited send‑off:

```py
import cowsay
import pyttsx3

engine = pyttsx3.init()
this = input("what's this? ")
cowsay.cow(this)
engine.say(this)
engine.runAndWait()
```

> Our hope is you’ll use these ideas to solve real problems and make the world a better place. **This was CS50!**
