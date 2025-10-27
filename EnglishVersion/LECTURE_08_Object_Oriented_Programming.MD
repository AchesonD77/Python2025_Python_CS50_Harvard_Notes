# Lecture 8 — Object-Oriented Programming (README)

> A faithful, cleaned, and searchable rendition of **Lecture 8**.  


## Contents
- [Object-Oriented Programming](#object-oriented-programming)
- [Classes](#classes)
- [`raise` (Exceptions)](#raise-exceptions)
- [Decorators / Properties](#decorators--properties)
- [Connecting to Previous Work](#connecting-to-previous-work)
- [Class Methods](#class-methods)
- [Static Methods](#static-methods)
- [Inheritance](#inheritance)
- [Inheritance and Exceptions](#inheritance-and-exceptions)
- [Operator Overloading](#operator-overloading)
- [Summing Up](#summing-up)

---

## Object-Oriented Programming
- Up to now: mostly **procedural** (step-by-step). OOP groups **data + behavior** and helps defend against errors.
- We’ll evolve a small script from procedural → functional abstraction → dictionaries → **classes**.

### Procedural start
```py
# student.py (procedural)
name = input("Name: ")
house = input("House: ")
print(f"{name} from {house}")
```
- Notice that this program follows a procedural, step-by-step paradigm: Much like you have seen in prior parts of this course.

### Abstract I/O into functions
- We can create functions to abstract away parts of this program.
```py
def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")

def get_name():
    return input("Name: ")

def get_house():
    return input("House: ")

if __name__ == "__main__":
    main()
```
- Notice how get_name and get_house abstract away some of the needs of our main function.
### Multiple returns with a tuple
- We can further simplify our program by storing the student as a tuple. A tuple is a sequence of values. Unlike a list, a tuple can’t be modified. In spirit, we are returning two values.

```py
def main():
    name, house = get_student()      # tuple unpacking
    print(f"{name} from {house}")

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house               # immutable
```
> *Note:* Tuples are **immutable**; lists are **mutable**.


- Packing that tuple, such that we are able to return both items to a variable called student, we can modify our code as follows.

```python
def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)


if __name__ == "__main__":
    main()
```

- Notice that (name, house) explicitly tells anyone reading our code that we are returning two values within one. Further, notice how we can index into tuples using student[0] or student[1].


- tuples are immutable, meaning we cannot change those values. Immutability is a way by which we can program defensively.
```python
def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house


if __name__ == "__main__":
    main()
```
- Notice that this code produces an error. Since tuples are immutable, we’re not able to reassign the value of student[1].


### List and dict variants (flexibility, Recall that dictionaries provide a key-value pair.)
```py
# List version (mutable)
def get_student():
    return [input("Name: "), input("House: ")]

# Dict version 00 (clearer semantics)
def get_student():
    return {"name": input("Name: "), "house": input("House: ")}

# Dice version 01
def get_student():
    student = {}  # we can remove the empty dictionary.
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student
```


- Note that lists are mutable. That is, the order of house and name can be switched by a programmer. You might decide to utilize this in some cases where you want to provide more flexibility at the cost of the security of your code. After all, if the order of those values is changeable, programmers that work with you could make mistakes down the road.

- Still, our code can be further improved. Notice that there is an unneeded variable. We can remove student = {} because we don’t need to create an empty dictionary.

- Notice we can utilize {} braces in the return statement to create the dictionary and return it all in the same line.

<mark>Why classes?</mark> To create our **own type** that can bundle data, enforce **invariants**, and provide **methods**.

---

## Classes
A **class** is a blueprint for objects (instances). Class names are Capitalized.
A class is like a mold for a type of data – where we can invent our own data type and give them a name.

```py
class Student:
    ...
```

### First refactor with attributes
```py
class Student:
    ...

def get_student():
    s = Student()
    s.name = input("Name: ")
    s.house = input("House: ")
    return s

def main():
    student = get_student()
    print(f"{student.name} from {student.house}")
```
- Notice by convention that Student is capitalized. Further, notice the ... simply means that we will later return to finish that portion of our code. Further, notice that in get_student, we can create a student of class Student using the syntax student = Student(). Further, notice that we utilize “dot notation” to access attributes of this variable student of class Student.

- Any time you create a class and you utilize that blueprint to create something, you create what is called an “object” or an “instance”. In the case of our code, student is an object.



### Constructor `__init__`
- Further, we can lay some groundwork for the attributes that are expected inside an object whose class is Student. We can modify our code as follows:

```py
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

def get_student():
    return Student(input("Name: "), input("House: "))
```
- Notice that within Student, we standardize the attributes of this class. We can create a function within class Student, called a “method”, that determines the behavior of an object of class Student. Within this function, it takes the name and house passed to it and assigns these variables to this object. Further, notice how the constructor student = Student(name, house) calls this function within the Student class and creates a student. self refers to the current object that was just created.

- Notice how return Student(name, house) simplifies the previous iteration of our code where the constructor statement was run on its own line.





### Printable representation `__str__`
```py
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    def __str__(self):
        return f"{self.name} from {self.house}"
```

> You can learn more in Python’s documentation of classes. https://docs.python.org/3/tutorial/classes.html

---

## `raise` (Exceptions)
Centralize validation *inside* the class and **raise** when invalid.

- Object-oriented programming encourages you to encapsulate all the functionality of a class within the class definition. What if something goes wrong? What if someone tries to type in something random? What if someone tries to create a student without a name? Modify your code as follows:

```py
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
```
- Notice how we check now that a name is provided and a proper house is designated. It turns out we can create our own exceptions that alerts the programmer to a potential error created by the user called raise. In the case above, we raise ValueError with a specific error message.


- It just so happens that Python allows you to create a specific function by which you can print the attributes of an object. Modify your code as follows

We can also extend the model with optional attributes + custom behavior:

```py
class Student:
    def __init__(self, name, house, patronus=None):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name, self.house, self.patronus = name, house, patronus

    def __str__(self): # here is print an object, its attributes, or almost anything you desire related to that object.
        return f"{self.name} from {self.house}"

    def charm(self):
        match self.patronus:
            case "Stag":                 return "🦌"
            case "Otter":                return "🦦"
            case "Jack Russell terrier": return "🐕"
            case _:                      return "✨"
```
- Notice how def __str__(self) provides a means by which a student is returned when called. Therefore, you can now, as the programmer, print an object, its attributes, or almost anything you desire related to that object.

- __str__ is a built-in method that comes with Python classes. It just so happens that we can create our own methods for a class as well!

- Notice how we define our own method charm. Unlike dictionaries, classes can have built-in functions called methods. In this case, we define our charm method where specific cases have specific results. Further, notice that Python has the ability to utilize emojis directly in our code.

- Notice how we have only two methods: __init__ and __str__.

---

## Decorators / Properties
*Goal:* keep dot syntax while validating on set. Use **`@property`** and store data in a “private-ish” attribute (e.g., `_house`).

```py
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Invalid name")
        self._name = name
        self.house = house  # invokes setter

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, v):
        if not v:
            raise ValueError("Invalid name")
        self._name = v

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, v):
        if v not in {"Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"}:
            raise ValueError("Invalid house")
        self._house = v
```

<mark>Rule of thumb:</mark> **Validate once** (inside setter/constructor) and reuse everywhere.

---

## Connecting to Previous Work
You’ve used classes all along:

```py
print(type(50))              # <class 'int'>
print(type("hello"))         # <class 'str'>
print(type([1,2,3]))         # <class 'list'>
print(type({"a": 1}))        # <class 'dict'>
```

Methods like `str.lower`, `list.append`, etc., are **class methods** on those built-ins.

---

## Class Methods
Use **`@classmethod`** to add behavior on the class as a whole.

```py
import random

class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

Hat.sort("Harry")
```

You can also use a classmethod as an **alternative constructor**:

```py
class Student:
    def __init__(self, name, house):
        self.name, self.house = name, house
    def __str__(self):
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)
```

---

## Static Methods
**`@staticmethod`** defines a namespaced utility that needs neither instance (`self`) nor class (`cls`) state. (Not shown in slides’ code, but useful to know.)

---

## Inheritance
Share/extend behavior across types.

```py
class Wizard:
    def __init__(self, name):
        if not name: raise ValueError("Missing name")
        self.name = name

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house

class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
```

---

## Inheritance and Exceptions
Exceptions form a **hierarchy** (e.g., `ValueError` ⊂ `Exception`). Catch a parent to handle children when appropriate. See Python docs for the full tree.

---

## Operator Overloading
Give your types arithmetic/text behavior via **dunder** methods.

```py
class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons, self.sickles, self.knuts = galleons, sickles, knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

    def __add__(self, other):
        return Vault(self.galleons + other.galleons,
                     self.sickles  + other.sickles,
                     self.knuts    + other.knuts)

potter  = Vault(100, 50, 25)
weasley = Vault(25, 50, 100)
print(potter)       # uses __str__
print(weasley)
print(potter + weasley)  # uses __add__
```

---

## Summing Up
- <mark>Core skills:</mark> **OOP**, **Classes**, **`raise`**, **`@property`**, **`@classmethod`/`@staticmethod`**, **Inheritance**, **Operator Overloading**.  
- *Design heuristics:* centralize validation, expose safe attributes via properties, prefer clear invariants, and overload responsibly.
