# Lecture 5 — Unit Tests, `assert`, `pytest`

## Table of Contents
- [Unit Tests](#unit-tests)
- [`assert`](#assert)
- [`pytest`](#pytest)
- [Testing Strings](#testing-strings)
- [Organizing Tests into Folders](#organizing-tests-into-folders)
- [Summing Up](#summing-up)

---

## Unit Tests

- Up to now, you may have been testing with `print` statements. In industry, we **write code to test our own code** (*unit tests*).
- Start with a tiny calculator:

```python
# calculator.py
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return n * n

if __name__ == "__main__":
    main()
```

- Create a test file following convention:

```python
# test_calculator.py
from calculator import square

def main():
    test_square()

def test_square():
    if square(2) != 4:
        print("2 squared was not 4")
    if square(3) != 9:
        print("3 squared was not 9")

if __name__ == "__main__":
    main()
```

- Running `python test_calculator.py` prints nothing if all is well, Alternatively, it could be that our test function did not discover one of the “corner cases” that could produce an error  — but this approach **doesn't scale**.

<mark>Key idea:</mark> Replace prints with **declarative expectations**.

---

## `assert`

- Python’s **`assert`** lets you state that a condition **must** hold.
- Python’s assert command allows us to tell the interpreter that something, some assertion, is true. 

```python
from calculator import square

def main():
    test_square()

def test_square():
    assert square(2) == 4
    assert square(3) == 9

if __name__ == "__main__":
    main()
```

- If an assertion fails, Python raises **`AssertionError`**.
- Essentially, this is the interpreter telling us that one of our conditions was not met.


Break the code intentionally to see it fail:

```python
# calculator.py (broken)
def square(n):
    return n + n  # <— bug: should be n * n
```

- You can also enumerate many cases (still manual and verbose):

```python
def test_square():
    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared is not 4")
    try:
        assert square(3) == 9
    except AssertionError:
        print("3 squared is not 9")
    try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squared is not 4")
    try:
        assert square(-3) == 9
    except AssertionError:
        print("-3 squared is not 9")
    try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared is not 0")
```

<mark>Takeaway:</mark> `assert` is concise, but **we still need a runner** to collect and report results elegantly.
- The above code illustrates a major challenge: How could we make it easier to test your code without dozens of lines of code like the above?
- You can learn more in Python’s documentation of assert. (https://docs.python.org/3/reference/simple_stmts.html#assert)

---

## `pytest`

- **`pytest`** is a third‑party framework that discovers and runs tests. Install with:
- That is, you can test your functions within your program.
```bash
pip install pytest
```

- Convert the single function into **separate test cases**:

```python
# test_calculator.py
from calculator import square

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0
```

Run:

```bash
pytest test_calculator.py
```

You’ll see failures when the implementation is buggy and clean output when fixed.

- In the terminal window, type pytest test_calculator.py. You’ll immediately notice that output will be provided. Notice the red F near the top of the output, indicating that something in your code failed. Further, notice that the red E provides some hints about the errors in your calculator.py program. Based upon the output, you can imagine a scenario where 3 * 3 has outputted 6 instead of 9. Based on the results of this test, we can go correct our calculator.py code as follows:


- Fix & break the implementation to observe results:

```python
# calculator.py (fixed)
def square(n):
    return n * n
```
- Re-running pytest test_calculator.py, notice how no errors are produced. Congratulations!
```python
# calculator.py (broken again to demo)
def square(n):
    return n + n
```

- To improve our test code, let’s modify test_calculator.py to divide the code into different groups of tests, Split tests into **groups** to keep output readable:

```python
from calculator import square

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0
```
- Notice that we have divided the same five tests into three different functions. Testing frameworks like pytest will run each function, even if there was a failure in one of them. Re-running pytest test_calculator.py, you will notice that many more errors are being displayed. More error output allows you to further explore what might be producing the problems within your code.
  

- Test that **exceptions** are raised using `pytest.raises`:

```python
import pytest
from calculator import square

def test_str():
    with pytest.raises(TypeError):
        square("cat")
```
- Notice that instead of using assert, we are taking advantage of a function within the pytest library itself called raises which allows you to express that you expect an error to be raised. We need to go to the top of our program and add import pytest and then call pytest.raises with the type of error we are expecting.


<mark>Tips:</mark> tests are just **functions starting with `test_`**; `pytest` runs **all of them**, even if one fails.
- You can learn more in Pytest’s documentation of pytest. (https://docs.pytest.org/en/7.1.x/getting-started.html)
---

## Testing Strings

Consider:
- Looking at this code, do you think that this approach to testing will work well? Why might this test not work well? Notice that the hello function in hello.py prints something: That is, it does not return a value!
```python
def main():
    name = input("What's your name? ")
    hello(name)


def hello(to="world"):
    print("hello,", to)


if __name__ == "__main__":
    main()
```
- We can change our hello function within hello.py as follows:
```python
# hello.py
def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print(f"hello, {to}")

if __name__ == "__main__":
    main()
```
- Notice that we changed our hello function to return a string. This effectively means that we can now use pytest to test the hello function.
  
- To test, **return** a value instead of printing:

```python
# hello.py (refactor)
def main():
    name = input("What's your name? ")
    print(hello(name))

def hello(to="world"):
    return f"hello, {to}"
```
- As with our previous test case in this lesson, we can break out our tests separately:
- Tests:

```python
# test_hello.py
from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("David") == "hello, David"
```

Run with:

```bash
pytest test_hello.py
```

- Notice that the above code separates our test into multiple functions such that they will all run, even if an error is produced.

<mark>Pattern:</mark> **Pure functions (return values)** are easier to unit test than functions that only print.

---

## Organizing Tests into Folders
- Unit testing code using multiple tests is so common that you have the ability to run a whole folder of tests with a single command.
  

- Create a folder and put tests inside it so `pytest` can run them all with one command:

```bash
mkdir test
code test/test_hello.py
```

`test/test_hello.py`:

```python
from hello import hello

def test_default():
    assert hello() == "hello, world"

def test_argument():
    assert hello("David") == "hello, David"
```

- Add an (even empty) `test/__init__.py` so discovery works reliably:
- pytest will not allow us to run tests as a folder simply with this file (or a whole set of files) alone without a special __init__ file. In your terminal window, create this file by typing code test/__init__.py. Note the test/ as before, as well as the double underscores on either side of init. Even leaving this __init__.py file empty, pytest is informed that the whole folder containing __init__.py has tests that can be run.

```bash
code test/__init__.py  # leave empty, or put package notes
```

Then run **all tests** in the folder:

```bash
pytest test
```

<mark>Convention:</mark> use names like **`test_*.py`** and **functions beginning with `test_`**.
- You can learn more in Pytest’s documentation of import mechanisms. (https://docs.pytest.org/en/7.1.x/explanation/pythonpath.html?highlight=folder#pytest-import-mechanisms-and-sys-path-pythonpath)
---

## Summing Up

Testing your code is a natural part of the programming process. Unit tests allow you to test specific aspects of your code. You can create your own programs that test your code. Alternatively, you can utilize frameworks like pytest to run your unit tests for you. In this lecture, you learned about…

- *Unit tests* to validate behavior.
- **`assert`** for declarative checks (fast feedback).
- **`pytest`** for discovery, grouping, and rich reporting.
- Testing *string‑producing* functions by returning values.
- Organizing tests into a **folder** with `__init__.py`.
