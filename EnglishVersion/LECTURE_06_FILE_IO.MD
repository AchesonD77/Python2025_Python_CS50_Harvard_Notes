# Lecture 6 — File I/O, CSV, Binary Files & PIL

## Table of Contents
- [File I/O](#file-io)
- [`open`](#open)
- [`with` context manager](#with-context-manager)
- [CSV](#csv)
- [Binary Files & PIL](#binary-files--pil)
- [Summing Up](#summing-up)

---

## File I/O

- So far, our programs stored data *only in memory*. When the program ends, data is lost. <mark>File I/O</mark> lets a program **read** from a file or **write** to a file.
- Start simple (`names.py`):

```python
name = input("What's your name? ")
print(f"hello, {name}")
```

- Collect multiple names using a list:

```python
names = []
for _ in range(3):
    name = input("What's your name? ")
    names.append(name)
```

- Print a **sorted** list:

```python
names = []
for _ in range(3):
    names.append(input("What's your name? "))

for name in sorted(names):
    print(f"hello, {name}")
```

<mark>Note:</mark> This is still in-memory; once the program finishes, inputs are lost — we need files.

- You can learn more in Python’s documentation of sorted. (https://docs.python.org/3/library/functions.html#sorted)
---

## `open`

- Python’s built‑in **`open`** opens a file for reading/writing.

Write one name to `names.txt` (overwrites file each run, mode `w`):

```python
name = input("What's your name? ")
file = open("names.txt", "w")
file.write(name)
file.close()
```
- Notice that the open function opens a file called names.txt with writing enabled, as signified by the w. The code above assigns that opened file to a variable called file. The line file.write(name) writes the name to the text file. The line after that closes the file.
- However, if you run your program multiple times using different names, you will notice that this program will entirely rewrite the names.txt file each time.

Append instead of overwriting (mode `a`), and add a newline:

```python
name = input("What's your name? ")
file = open("names.txt", "a")
file.write(name)
file.close()
```
- Examining your text file after running your program multiple times, you’ll notice that the names are running together. The names are being appended without any gaps between each of the names. 
```python
name = input("What's your name? ")
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()
```
- Notice that the line with file.write has been modified to add a line break at the end of each name.


<mark>Common pitfall:</mark> forgetting to `close()` the file.
- You can learn more in Python’s documentation of open. (https://docs.python.org/3/library/functions.html#open)
---

## `with` context manager

- Use **`with`** to manage files safely (auto‑close) and read them back.

Write:

```python
name = input("What's your name? ")
with open("names.txt", "a") as file:
    file.write(f"{name}\n")
```
- Notice that the line below with is indented.


- What if we want to read from a file? 

Read all lines (and here is a simple way to fix this error in our code: strip trailing newlines):

```python
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.rstrip())
```
- Notice that rstrip has the effect of removing the extraneous line break at the end of each line.

- Still, this code could be simplified even further:
```python
with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())
```
- However, notice that we are not sorting the names.

Sort while reading:

```python
names = []
with open("names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")
```
- Notice that names is a blank list where we can collect the names. Each name is appended to the names list in memory. Then, each name in the sorted list in memory is printed. Running your code, you will see that the names are now properly sorted.

<mark>Tip:</mark> `rstrip()` removes the extra newline at the end of each line.

---

## CSV

- **CSV** = *comma‑separated values*.
- Create `students.csv`:

```
Hermione,Gryffindor
Harry,Gryffindor
Ron,Gryffindor
Draco,Slytherin
```

Read the file by splitting each line:

```python
with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")
```

- Notice that rstrip removes the end of each line in our CSV file. split tells the interpreter where to find the end of each of our values in our CSV file. row[0] is the first element in each line of our CSV file. row[1] is the second element in each line in our CSV file.



- Python has built-in ability that could further simplify this code. 

Unpack directly to two variables:

```python
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")
```
- Notice that the split function actually returns two values: The one before the comma and the one after the comma. Accordingly, we can rely upon that functionality to assign two variables at once instead of one!


Collect to structures for sorting and later use:

```python
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)
```
- Notice that we create a list called students. We append each string to this list. Then, we output a sorted version of our list.


Recall that Python allows for dictionaries where a key can be associated with a value. This code could be further improved

```python
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["house"] = house
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")
```
- Notice that we create an empty dictionary called student. We add the values for each student, including their name and house into the student dictionary. Then, we append that student to the list called students.

We can improve our code to illustrate this as follows:
```python
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for student in students:
    print(f"{student['name']} is in {student['house']}")
```
- Notice that this produces the desired outcome, minus the sorting of students.
- Unfortunately, we cannot sort the students as we had prior because **each student is now a dictionary inside of a list**. It would be helpful if Python could sort the students list of student dictionaries that sorts this list of dictionaries by the student’s name.

To implement this in our code, make the following changes:
```python
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append({"name": name, "house": house})


def get_name(student):
    return student["name"]


for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")
```
- Notice that sorted needs to know how to get the key of each student. Python allows for a parameter called key where we can define on what “key” the list of students will be sorted. Therefore, the get_name function simply returns the key of student["name"]. Running this program, you will now see that the list is now sorted by name.

Still, our code can be further improved upon. It just so happens that if you are only going to use a function like get_name once, you can simplify your code in the manner presented below. Modify your code as follows:
```python
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append({"name": name, "house": house})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
```
- Notice how we use a lambda function, an anonymous function, that says “Hey Python, here is a function that has no name: Given a student, access their name and return that to the key.

Unfortunately, our code is a bit fragile. Suppose that we changed our CSV file such that we indicated where each student grew up. What would be the impact of this upon our program? First, modify your students.csv file as follows:

```
Harry,"Number Four, Privet Drive"
Ron,The Burrow
Draco,Malfoy Manor
```
- The ValueError: too many values to unpack error produced by the interpreter is a result of the fact that we previously created this program expecting the CSV file is split using a , (comma). We could spend more time addressing this, but indeed someone else has already developed a way to “parse” (that is, to read) CSV files!

- Python’s built-in csv library comes with an object called a reader. As the name suggests, we can use a reader to read our CSV file despite the extra comma in “Number Four, Privet Drive”. A reader works in a for loop, where each iteration the reader gives us another row from our CSV file. This row itself is a list, where each value in the list corresponds to an element in that row. row[0], for example, is the first element of the given row, while row[1] is the second element.


<mark>Edge case:</mark> if a field contains a comma (e.g., *"Number Four, Privet Drive"*), manual `split(",")` breaks. Use the **`csv`** module.

Using `csv.reader`:
```python
import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({"name": row[0], "home": row[1]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
```


Up until this point, we have been relying upon our program to specifically decide what parts of our CSV file are the names and what parts are the homes. It’s better design, though, to bake this directly into our CSV file by editing it as follows:
```
name,home
Harry,"Number Four, Privet Drive"
Ron,The Burrow
Draco,Malfoy Manor
```
- We can modify our code to use a part of the csv library called a DictReader to treat our CSV file with even more flexibilty:

Using `csv.DictReader` (reads each row as a dict using header names):

```python
import csv

students = []
with open("students.csv") as file:
    reader = csv.DictReader(file)   # requires header row: name,home
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")
```
- Notice that we have replaced reader with DictReader, which returns one dictionary at a time. Also, notice that the interpreter will directly access the row dictionary, getting the name and home of each student. This is an example of coding defensively. As long as the person designing the CSV file has inputted the correct header information on the first line, we can access that information using our program.

What if we want to write to a CSV file?

Writing CSV with `DictWriter`:

```python
import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
```

- Notice how we are leveraging the built-in functionality of DictWriter, which takes two parameters: the file being written to and the fieldnames to write. Further, notice how the writerow function takes a dictionary as its parameter. Quite literally, we are telling the interpreter to write a row with two fields called name and home.

<mark>Best practices:</mark> prefer `csv` to handle quoting, embedded commas, and newlines.
- Note that there are many types of files that you can read from and write to.
- You can learn more in Python’s documentation of CSV. https://docs.python.org/3/library/csv.html
---

## Binary Files & PIL

- A **binary file** stores bytes (0s/1s): images, audio, video, etc.
- There is a popular Python library called PIL that works well with image files.
- Using **Pillow (PIL)** to build an animated GIF from frames:

```python
# pip install pillow
import sys
from PIL import Image

images = []
for arg in sys.argv[1:]:         # collect image paths from CLI
    img = Image.open(arg)
    images.append(img)

images[0].save(
    "costumes.gif",
    save_all=True,
    append_images=images[1:],
    duration=200,
    loop=0,
)
```
- Notice that we import the Image functionality from PIL. Notice that the first for loop simply loops through the images provided as command-line arguments and stores theme into the list called images. The 1: starts slicing argv at its second element. The last lines of code saves the first image and also appends a second image to it as well, creating an animated gif. Typing python costumes.py costume1.gif costume2.gif into the terminal. Now, type code costumes.gif into the terminal window, and you can now see an animated GIF.

Run:

```bash
python costumes.py costume1.gif costume2.gif
```

<mark>Notes:</mark> `save_all=True` makes an animated GIF; `duration` controls frame delay; `loop=0` loops forever.

You can learn more in Pillow’s documentation of PIL. (https://pillow.readthedocs.io/)

---

## Summing Up

Now, we have not only seen that we can write and read files textually—we can also read and write files using ones and zeros. We can’t wait to see what you achieve with these new abilities next.

You learned how to…

- Perform **File I/O** (read/write)
- Use **`open`** safely with *modes* (`"w"`, `"a"`, `"r"`)
- Prefer **`with`** to auto‑close files
- Parse and write **CSV** with the `csv` module (`reader`, `DictReader`, `DictWriter`)
- Work with **binary files** and **PIL** to create an animated GIF
