# Lecture 8 — Object-Oriented Programming (README)

> A faithful, cleaned, and searchable rendition of **Lecture 8** based on your screenshots.  
> Emphasis legend: *italics*, **bold**, and <mark>highlight</mark> for must‑know ideas.

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

### Abstract I/O into functions
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

### Multiple returns with a tuple
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

### List and dict variants
```py
# List version (mutable)
def get_student():
    return [input("Name: "), input("House: ")]

# Dict version (clearer semantics)
def get_student():
    return {"name": input("Name: "), "house": input("House: ")}
```

<mark>Why classes?</mark> To create our **own type** that can bundle data, enforce **invariants**, and provide **methods**.

---

## Classes
A **class** is a blueprint for objects (instances). Class names are Capitalized.

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

### Constructor `__init__`
```py
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

def get_student():
    return Student(input("Name: "), input("House: "))
```

### Printable representation `__str__`
```py
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house
    def __str__(self):
        return f"{self.name} from {self.house}"
```

---

## `raise` (Exceptions)
Centralize validation *inside* the class and **raise** when invalid.

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

We can also extend the model with optional attributes + custom behavior:

```py
class Student:
    def __init__(self, name, house, patronus=None):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name, self.house, self.patronus = name, house, patronus

    def __str__(self):
        return f"{self.name} from {self.house}"

    def charm(self):
        match self.patronus:
            case "Stag":                 return "🦌"
            case "Otter":                return "🦦"
            case "Jack Russell terrier": return "🐕"
            case _:                      return "✨"
```

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
