# Lecture 2 — Loops

## Table of Contents
- [Loops](#loops)
- [While Loops](#while-loops)
- [For Loops](#for-loops)
- [Improving with User Input](#improving-with-user-input)
- [More About Lists](#more-about-lists)
- [Length](#length)
- [Dictionaries](#dictionaries)
- [Mario](#mario)
- [Summing Up](#summing-up)

---

## Loops

- Essentially, **loops** are a way to *do something over and over again*.
- Begin by creating `cat.py` in your terminal.
- Start with:

```python
print("meow")
print("meow")
print("meow")
```

- Running `python cat.py` prints three meows. But writing the same line repeatedly is not scalable (imagine 500!).
- **Loops** let you create a block of code that executes repeatedly.

---

## While Loops

- The **`while`** loop repeats a block *while* a condition is `True`.
- Example with a bug (infinite loop):

```python
i = 3
while i != 0:
    print("meow")
```
- Notice how even though this code will execute print("meow") multiple times, it will never stop! It will loop forever. while loops work by repeatedly asking if the condition of the loop has been fulfilled. In this case, the interpreter is asking, “does i not equal zero?” When you get stuck in a loop that executes forever, you can press Ctrl+C on your keyboard to break out of the loop.



- Fix by changing the loop variable each iteration:

```python
i = 3
while i != 0:
    print("meow")
    i = i - 1
```
- Notice that now our code executes properly, reducing i by 1 for each “iteration” through the loop. The term iteration has special significance within coding. By iteration, we mean one cycle through the loop. The first iteration is the “0th” iteration through the loop. The second is the “1st” iteration. In programming, we count starting with 0, then 1, then 2.
  

- Prefer counting from **0** (best practice) and iterating **up**:

```python
i = 1
while i <= 3:
    print("meow")
    i = i + 1
```

- Even better—start from 0 and use `i += 1`:

```python
i = 0
while i < 3:
    print("meow")
    i += 1
```

> The loop counts *up to* but not through 3.

---

## For Loops

- A **`for`** loop iterates through a **list** (or any iterable).
- To best understand a for loop, it’s best to begin by talking about a new variable type called a list in Python. As in other areas of our lives, we can have a grocery list, a to-do list, etc.
- Minimal list example:

```python
for i in [0, 1, 2]:
    print("meow")
```
- At first glance, our code looks great. However, what if you wanted to iterate up to a million? 
  

- Cleaner, scalable approach: `range(3)` automatically gives `0, 1, 2`:

```python
for i in range(3):
    print("meow")
```


- In Python, if such a variable does not have any other significance in our code, we can simply represent this variable as a single underscore _.
- If the loop variable is unused, adopt the conventional underscore:

```python
for _ in range(3):
    print("meow")
```

- Multiplying strings repeats them:

```python
print("meow" * 3)
```

- Add a newline at the end of each meow:

```python
print("meow\n" * 3, end="")
```
- Notice how this code produces three meows, each on a separate line. By adding end="" and the \n we tell the interpreter to add a line break at the end of each meow.


---

## Improving with User Input

- A common paradigm within Python is to use a while loop to validate the input of the user.
- Use loops to validate input; for instance, require **`n >= 0`**:

```python
while True:
    n = int(input("What's n? "))
    if n < 0:
        continue
    else:
        break
```
- Notice that we’ve introduced two new keywords in Python, continue and break.
- `continue` jumps to the next iteration; `break` exits the loop.  
  In this case `continue` is **redundant**—streamline:

```python
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")
```

- Encapsulate logic into **functions** and return values:

```python
def main():
    meow(get_number())

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")

main()
```

- Notice how not only did we change your code to operate in multiple functions, but we also used a return statement to return the value of n back to the main function.
---

## More About Lists

- Consider Hogwarts students.

```python
students = ["Hermione", "Harry", "Ron"]

print(students[0])
print(students[1])
print(students[2])
```
- Notice how we have a list of students with their names as above. We then print the student who is at the 0th location, “Hermione”. Each of the other students is printed as well.
  

- Iterate the list directly:

```python
students = ["Hermione", "Harry", "Ron"]

for student in students:
    print(student)
```
- Notice that for each student in the students list, it will print the student as intended. You might wonder why we did not use the _ designation as discussed prior. We choose not to do this because student is explicitly used in our code.
  
- Docs tip: lists are ordered and indexable. *Use `for … in …` when you don’t need indices.*


- You can learn more in Python’s documentation of lists.(https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)
---

## Length

- Use **`len`** to get list length and index while printing names and positions:

```python
students = ["Hermione", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])
```
- Notice how executing this code results in not only getting the position of each student plus one using i + 1, but also prints the name of each student. len allows you to dynamically see how long the list of the students is regardless of how much it grows.



- <mark>**Prefer**</mark> direct iteration when indices aren’t needed; use `range(len(…))` when you *do* need them.
- You can learn more in Python’s documentation of len.(https://docs.python.org/3/library/functions.html?highlight=len#len)
---

## Dictionaries

- A **`dict`** associates keys with values.
```
dicts or dictionaries are a data structure 
that allows you to associate keys with values.

Where a list is a list of multiple values, 
a dict associates a key with a value.


```

- Parallel lists version (hard to maintain as it grows):
```python
students = ["Hermione", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]
```
- Notice that we can promise that we will always keep these lists in order. The individual at the first position of students is associated with the house at the first position of the houses list, and so on. However, this can become quite cumbersome as our lists grow!
  

- Prefer a dictionary:

```python
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}
print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])
```
- Notice how we use {} curly braces to create a dictionary. Where lists use numbers to iterate through the list, dicts allow us to use words.
  

- Looping keys only:

```python
for student in students:
    print(student)
```

- Keys + values (clean output with a comma separator):

```python
for student in students:
    print(student, students[student], sep=", ")
```
- Notice how students[student] will go to each student’s key and find the value of their house. 
  

- Toward *richer* data: a **list of dicts** with multiple keys per student:

```python
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
```
- Notice how this code creates a list of dicts. The list called students has four dicts within it: One for each student. Also, notice that Python has a special None designation where there is no value associated with a key.
- Notice how the for loop will iterate through each of the dicts inside the list called students.


- You can learn more in Python’s Documentation of dicts.(https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
---

## Mario

- The classic game *Mario* shows a hero jumping over bricks. Let’s print bricks with loops.

```python
print("#")
print("#")
print("#")
```

- Replace repetition with a **for** loop:

```python
for _ in range(3):
    print("#")
```

- Abstract into functions to print a **column** of any height:

```python
def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")

main()
```

- Print a **row** horizontally:

```python
def main():
    print_row(4)

def print_row(width):
    print("?" * width)

main()
```

- Rows *and* columns (nested loops) to draw a square:

```python
def main():
    print_square(3)

def print_square(size):
    # For each row in square
    for i in range(size):
        # For each brick in row
        for j in range(size):
            # Print brick
            print("#", end="")
        # Print blank line
        print()

main()
```

- We can further abstract away our code:

```python
def main():
    print_square(3)


def print_square(size):
    for i in range(size):
        print_row(size)


def print_row(width):
    print("#" * width)


main()
```

---

## Summing Up

You now have another power in your growing list of Python abilities. In this lecture, we addressed…

- **<mark>Loops</mark>**
- **`while`**
- **`for`**
- **`len`**
- **`list`**
- **`dict`**
