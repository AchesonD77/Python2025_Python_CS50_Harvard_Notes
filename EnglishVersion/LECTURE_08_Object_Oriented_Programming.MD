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
- Properties can be utilized to harden our code. In Python, we define properties using function “decorators”, which begin with @.
- In addition to the name of the house, we can protect the name of our student as well. Modify your code as follows:

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

def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
```
> The text explains the use of the @property decorator in Python to define class attributes, enabling a more controlled and Pythonic way of interacting with an object's state.

> 1. Defining a Property (@property): By placing @property above a function (e.g., house), the function is converted into a class property. Accessing the attribute (e.g., student.house) now calls this property's getter function.
> 2. The Setter (@house.setter): A setter function is defined using the @property_name.setter decorator. This function is automatically called whenever the property is assigned a new value (e.g., student.house = "Gryffindor").
> 3. Encapsulation and Validation: The setter's primary role is to validate the input value. The example shows how the setter checks if the assigned value is one of the valid "Harry Potter houses" and raises a ValueError if it's not.
> 4. The Internal Attribute (_house): The property manages the actual data through an internal class attribute, typically named with a leading underscore (e.g., _house). This underscore indicates that the attribute is private/protected and should only be modified via the defined setter method, not directly by the user.

- You can learn more in Python’s documentation of methods. https://docs.python.org/3/tutorial/classes.html

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

- Sometimes, we want to add functionality to a class itself, not to instances of that class.
- @classmethod is a function that we can use to add functionality to a class as a whole.


- Here’s an example of not using a class method. In your terminal window, type code hat.py and code as follows:

```python
import random


class Hat:
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def sort(self, name):
        print(name, "is in", random.choice(self.houses))


hat = Hat()
hat.sort("Harry")
```
- Notice how when we pass the name of the student to the sorting hat, it will tell us what house is assigned to the student. Notice that hat = Hat() instantiates a hat. The sort functionality is always handled by the instance of the class Hat. By executing hat.sort("Harry"), we pass the name of the student to the sort method of the particular instance of Hat, which we’ve called hat.
  


- We may want, though, to run the sort function without creating a particular instance of the sorting hat (there’s only one, after all!). We can modify our code as follows:
```py
import random

class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

Hat.sort("Harry")
```
- Notice how the __init__ method is removed because we don’t need to instantiate a hat anywhere in our code. self, therefore, is no longer relevant and is removed. We specify this sort as a @classmethod, replacing self with cls. Finally, notice how Hat is capitalized by convention near the end of this code, because this is the name of our class.


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

- Notice that get_student is removed and a @classmethod called get is created. This method can now be called without having to create a student first.

---

## Static Methods
**`@staticmethod`** defines a namespaced utility that needs neither instance (`self`) nor class (`cls`) state. (Not shown in slides’ code, but useful to know.)

---

## Inheritance
Share/extend behavior across types.
- Inheritance is, perhaps, the most powerful feature of object-oriented programming.
- It just so happens that you can create a class that “inherits” methods, variables, and attributes from another class.
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
- Notice that there is a class above called Wizard and a class called Student. Further, notice that there is a class called Professor. Both students and professors have names. Also, both students and professors are wizards. Therefore, both Student and Professor inherit the characteristics of Wizard. Within the “child” class Student, Student can inherit from the “parent” or “super” class Wizard as the line super().\__init__(name) runs the init method of Wizard. Finally, notice that the last lines of this code create a wizard called Albus, a student called Harry, and so on.


---

## Inheritance and Exceptions
Exceptions form a **hierarchy** (e.g., `ValueError` ⊂ `Exception`). Catch a parent to handle children when appropriate. See Python docs for the full tree.
- While we have just introduced inheritance, we have been using this all along during our use of exceptions.
- It just so happens that exceptions come in a hierarchy, where there are children, parent, and grandparent classes. These are illustrated below:
```
  BaseException
 +-- KeyboardInterrupt
 +-- Exception
      +-- ArithmeticError
      |    +-- ZeroDivisionError
      +-- AssertionError
      +-- AttributeError
      +-- EOFError
      +-- ImportError
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- KeyError
      +-- NameError
      +-- SyntaxError
      |    +-- IndentationError
      +-- ValueError
 ...
 ```
- You can learn more in Python’s documentation of exceptions. https://docs.python.org/3/library/exceptions.html

## Operator Overloading
Give your types arithmetic/text behavior via **dunder** methods.
- Some operators such as + and - can be “overloaded” such that they can have more abilities beyond simple arithmetic.

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
- Notice how the __str__ method returns a formatted string. Further, notice how the __add__ method allows for the addition of the values of two vaults. self is what is on the left of the + operand. other is what is right of the +.

- You can learn more in Python’s documentation of operator overloading. https://docs.python.org/3/reference/datamodel.html#special-method-names
---

## Summing Up
- Now, you’ve learned a whole new level of capability through object-oriented programming.
  
- <mark>Core skills:</mark> **OOP**, **Classes**, **`raise`**, **`@property`**, **`@classmethod`/`@staticmethod`**, **Inheritance**, **Operator Overloading**.  
- *Design heuristics:* centralize validation, expose safe attributes via properties, prefer clear invariants, and overload responsibly.
```
Object-oriented programming
Classes
raise
Class Methods
Static Methods
Inheritance
Operator Overloading
```