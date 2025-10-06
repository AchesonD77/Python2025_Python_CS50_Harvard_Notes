# Lecture 4 — Libraries, Randomness, CLI, Packages, APIs

## Table of Contents
- [Libraries](#libraries)
- [Random](#random)
- [Statistics](#statistics)
- [Command-Line Arguments](#command-line-arguments)
- [Slice](#slice)
- [Packages](#packages)
- [APIs](#apis)
- [Making Your Own Libraries](#making-your-own-libraries)
- [Summing Up](#summing-up)

---

## Libraries

- In Python, **libraries (modules)** are bits of code written by you or others that you can reuse.
- Python allows you to share functions or features with others as *modules*.
- You can also extract code from an old project to create a **module** or **library** for a new project.

---

## Random
- Random is a library that comes with Python that you could import into your own project.
- So, how do you load a module into your own program? You can use the word import in your program.
  

- Inside the random module, there is a built-in function called random.choice(seq). random is the module you are importing. Inside that module, there is the choice function. That function takes into it a seq or sequence that is a list.
- The built‑in **`random`** library lets you generate random choices and numbers.

**`random.choice(seq)`** — choose one item from a sequence (list/tuple).

```python
import random

coin = random.choice(["heads", "tails"])
print(coin)
```

- We can improve our code. from allows us to be very specific about what we’d like to import. Prior, our import line of code is bringing the entire contents of the functions of random. However, what if we want to only load a small part of a module? Modify your code as follows:

- Importing *a single name* saves resources and clarifies intent:

```python
from random import choice

coin = choice(["heads", "tails"])
print(coin)
```
- Notice that we now can import just the choice function of random. From that point forward, we no longer need to code random.choice.
- We can now only code choice alone. choice is loaded explicitly into our program. This saves system resources and potentially can make our code run faster!


**`random.randint(a, b)`** — random integer in the **inclusive** range `[a, b]`.

```python
from random import randint

number = randint(1, 10)
print(number)
```
- Notice that our code will randomly generate a number between 1 and 10.

**`random.shuffle(list)`** — shuffle a list *in place* (returns `None`).

```python
import random

cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
```
- Notice that random.shuffle will shuffle the cards in place. Unlike other functions, it will not return a value. Instead, it will take the cards list and shuffle them inside that list. Run your code a few times to see the code functioning.

<mark>Takeaway:</mark> **`choice`**, **`randint`**, and **`shuffle`** are three quick ways to create randomness.

Docs: Python `random` module (https://docs.python.org/3/library/random.html).

---

## Statistics

- Python ships with **`statistics`**. A handy function is **`mean`**:

```python
import statistics

print(statistics.mean([100, 90]))
```
- Notice that we imported a different library called statistics. The mean function takes a list of values. This will print the average of these values. In your terminal window, type python average.py.
  

- Consider using `statistics` in your own programs when average or variance is needed.
- Docs: Python `statistics` module (https://docs.python.org/3/library/statistics.html).

---

## Command-Line Arguments

- We can accept **command‑line arguments** via the **`sys`** module and `sys.argv` list.
- argv is a list within the sys module that records what the user typed on the command line.

```python
import sys

print("hello, my name is", sys.argv[1])
```
- Notice that sys.argv[1] is where David is being stored. Why is that? Well, in prior lessons, you might remember that lists start at the 0th element. What do you think is held currently in sys.argv[0]? If you guessed name.py, you would be correct!


- `sys.argv[0]` is the program name; the *first* real argument is `sys.argv[1]`.


- There is a small problem with our program as it stands. What if the user does not type in the name at the command line? Try it yourself. Type python name.py into the terminal window. An error list index out of range will be presented by the interpreter. The reason for this is that there is nothing at sys.argv[1] because nothing was typed! Here’s how we can protect our program from this type of error:
- Guard against missing arguments using **exceptions**:

```python
import sys

try:
    print("hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")
```

- A more defensive approach uses **length checks** and **early exit** with `sys.exit`:

```python
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many arguments")

print("hello, my name is", sys.argv[1])
```

- `sys.exit` terminates the program immediately; the final `print` runs only when the input is valid.
- Docs: Python `sys` module. (https://docs.python.org/3/library/sys.html)

---

## Slice

- slice is a command that allows us to take a list and tell the interpreter where we want the interpreter to consider the start of the list and the end of the list. For example, modify your code as follows:
- **Slice** syntax lets us take a *portion* of a list, e.g., `sys.argv[1:]` skips the script name.

```python
import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for arg in sys.argv[1:]:
    print("hello, my name is", arg)
```
- Notice that rather than starting the list at 0, we use square brackets to tell the interpreter to start at 1 and go to the end using the 1: argument. Running this code, you’ll notice that we can improve our code using relatively simple syntax.

- <mark>Note:</mark> `list[start:end]` is half‑open; omit `end` to go to the list’s end.

---

## Packages
- One of the reasons Python is so popular is that there are numerous powerful third-party libraries that add functionality. We call these third-party libraries, implemented as a folder, “packages”.
  
- Third‑party packages extend Python’s capabilities. They’re published on **PyPI** and installed via **`pip`**.
- Example: **`cowsay`** (a playful library that makes a cow speak).

```bash
pip install cowsay
```

```python
import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.cow("hello, " + sys.argv[1])
```

- Other variants exist (e.g., the *t‑rex*): 

```python
import cowsay, sys

if len(sys.argv) == 2:
    cowsay.trex("hello, " + sys.argv[1])
```

- Learn more packages at <mark>PyPI</mark>. (https://pypi.org/)

---

## APIs

- **APIs** (*application programming interfaces*) let your program communicate with other services, allow you to connect to the code of others.
- The **`requests`** package behaves like a browser to fetch data from the web.

Install once:

```bash
pip install requests
```

Basic usage—query Apple iTunes Search API:

```python
import requests, sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]
)
print(response.json())
```
- It turns out that Apple iTunes has its own API that you can access in your programs. In your internet browser, you can visit https://itunes.apple.com/search?entity=song&limit=1&term=weezer and a text file will be downloaded. David constructed this URL by reading Apple’s API documentation. Notice how this query is looking for a song, with a limit of one result, that relates to the term called weezer. Looking at this text file that is downloaded, you might find the format to be similar to that we’ve programmed previously in Python.
  

- The format in the downloaded text file is called JSON, a text-based format that is used to exchange text-based data between applications. Literally, Apple is providing a JSON file that we could interpret in our own Python program.
- The returned JSON can be pretty‑printed via the standard **`json`** module:

```python
import json, requests, sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]
)
print(json.dumps(response.json(), indent=2))
```

- Extract the track name from multiple results (increase `limit` to 50):

```python
import json, requests, sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1]
)
o = response.json()
for result in o["results"]:
    print(result["trackName"])
```
- Notice how we are taking the result of response.json() and storing it in o (as in the lowercase letter). Then, we are iterating through the results in o and printing each trackName. Also notice how we have increased the limit number of results to 50. Run your program. See the results.
  

- Docs: `requests` user guide (https://docs.python-requests.org/); Python `json` docs (https://docs.python.org/3/library/json.html).

---

## Making Your Own Libraries

- You can create your **own library** to reuse code.

`sayings.py`:

```python
def hello(name):
    print(f"hello, {name}")

def goodbye(name):
    print(f"goodbye, {name}")
```

Use it from another file `say.py`:

```python
import sys
from sayings import goodbye

if len(sys.argv) == 2:
    goodbye(sys.argv[1])
```

- <mark>Key idea:</mark> factor reusable functions into modules and import them where needed.

---

## Summing Up
Libraries extend the abilities of Python. Some libraries are included by default with Python and simply need to be imported. Others are third-party packages that need to be installed using pip. You can make your own packages for use by yourself or others! In this lecture, you learned about…


- **Libraries**
- **Random** (`choice`, `randint`, `shuffle`)
- **Statistics** (`mean`)
- **Command‑Line Arguments** (`sys.argv`, `sys.exit`)
- **Slice** (`argv[1:]`)
- **Packages** (PyPI, `pip`, `cowsay`)
- **APIs** (`requests`, `json`, iTunes Search)
- **Making Your Own Libraries**
