# Lecture 7 — Regular Expressions, Cleaning Input, Extracting Data

> *Goal:* learn to **validate**, **clean**, and **extract** user input with Python’s `re` module.

## Table of Contents
- [Regular Expressions](#regular-expressions)
- [Case Sensitivity](#case-sensitivity)
- [Cleaning Up User Input](#cleaning-up-user-input)
- [Extracting User Input](#extracting-user-input)
- [Summing Up](#summing-up)

- reference: https://cs50.harvard.edu/python/notes/7/

---

## Regular Expressions

Regular expressions (*regexes*) let us detect patterns in text. We’ll start from naive checks and iterate toward robust validation.

### 1) Naive checks
```py
email = input("What's your email? ").strip()
if "@" in email:
    print("Valid")
else:
    print("Invalid")
```
- Problem: `@` alone is accepted. We can require both `@` and `.`:
```py
email = input("What's your email? ").strip()
if "@" in email and "." in email:
    print("Valid")
else:
    print("Invalid")
```
Still weak (e.g., `@` in wrong place).

### 2) Split into parts
```py
email = input("What's your email? ").strip()
username, domain = email.split("@")
if username and "." in domain:
    print("Valid")
else:
    print("Invalid")
```
Better, but **still** accepts bad domains (e.g., `malan@harvard?edu`).

```python
email = input("What's your email? ").strip()

username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")
```
- Notice how the endswith method will check to see if domain contains .edu. Still, however, a nefarious user could still break our code. For example, a user could type in malan@.edu and it would be considered valid.

### 3) Enter `re.search`
- Python has an existing library called re that has a number of built-in functions that can validate user inputs against patterns.

<mark>Core idea:</mark> match **patterns**, not substrings.
```py
import re

email = input("What's your email? ").strip()
if re.search(r"@.+", email):
    print("Valid")
else:
    print("Invalid")
```
The pattern now matters. We can grow vocabulary:

- `.` any char except newline  
- `*` 0+ repetitions, `+` 1+ repetitions, `?` 0/1 repetition  
- `{m}` exactly m, `{m,n}` m–n  
- `^` start of string, `$` end of string  
- Character classes: `[abc]`, `[^abc]`, `[a-zA-Z0-9_]`, `\w` word, `\W` non-word, `\d` digit, `\D` non-digit, `\s` whitespace, `\S` non-whitespace.

```python
import re

email = input("What's your email? ").strip()

if re.search(".+@.+.edu", email):
    print("Valid")
else:
    print("Invalid")
```

Notice, however, that one could type in malan@harvard?edu and it could be considered valid. Why is this the case? You might recognize that in the language of validation, a . means any character!

We can modify our code as follows:
```python
import re

email = input("What's your email? ").strip()

if re.search(r".+@.+\.edu", email):
    print("Valid")
else:
    print("Invalid")
```

Notice how we utilize the “escape character” or \ as a way of regarding the . as part of our string instead of our validation expression. Testing your code, you will notice that malan@harvard.edu is regarded as valid, where malan@harvard?edu is invalid.


Now that we’re using escape characters, it’s a good time to introduce “raw strings”. In Python, raw strings are strings that don’t format special characters—instead, each character is taken at face-value. Imagine \n, for example. We’ve seen in an earlier lecture how, in a regular string, these two characters become one: a special newline character. In a raw string, however, \n is treated not as \n, the special character, but as a single \ and a single n. Placing an r in front of a string tells the Python interpreter to treat the string as a raw string, similar to how placing an f in front of a string tells the Python interpreter to treat the string as a format string:
```python
import re

email = input("What's your email? ").strip()

if re.search(r"^.+@.+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
```
Now we’ve ensured the Python interpreter won’t treat \. as a special character. Instead, simply as a \ followed by a .—which, in regular expression terms, means matching a literal “.”.

It just so happens we have more special symbols at our disposal in validation:

```
^   matches the start of the string
$   matches the end of the string or just before the newline at the end of the string
```

Notice this has the effect of looking for this exact pattern matching to the start and end of the expression being validated. Typing in a sentence such as My email address is malan@harvard.edu. now is regarded as invalid.


### 4) Tighten the email
```py
import re
email = input("What's your email? ").strip()

# Allow letters/digits/underscore in the user, simple domain with .edu
if re.search(r"^[\w]+@[\w]+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
```
- `^...$` anchors make sure the whole string matches.
- Use **raw strings** like `r"...“` so backslashes are not eaten by Python.

### 5) More realistic TLDs
```py
if re.search(r"^[\w]+@[\w]+\.(com|edu|gov|net|org)$", email):
    ...
```
- `|` is logical *or* inside a group.
- For richer usernames and domains:
```py
if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.[a-zA-Z]{2,}$", email):
    ...
```
- <mark>Important:</mark> prefer **`re.fullmatch`** when you want the entire string to match:
```py
if re.fullmatch(r"[A-Za-z0-9_]+@[A-Za-z0-9_]+\.[A-Za-z]{2,}", email):
    print("Valid")
else:
    print("Invalid")
```

Now, we know that there are not simply .edu email addresses. We could modify our code as follows:

```python
import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@\w.+\.(com|edu|gov|net|org)$", email):
    print("Valid")
else:
    print("Invalid")
```
Notice that the | has the impact of an or in our expression.

Adding even more symbols to our vocabulary, here are some more to consider:
```
A|B     either A or B
(...)   a group
(?:...) non-capturing version
```

## Case Sensitivity

`re` is case‑sensitive by default. Use flags:
```py
import re
if re.search(r"^[\w]+@[\w]+\.edu$", email, re.IGNORECASE):
    print("Valid (case-insensitive)")
```
Other handy flags: `re.MULTILINE`, `re.DOTALL`.

- Some built-in flag variables are:
```python
re.IGNORECASE
re.MULTILINE
re.DOTALL
```
- Therefore, we can change our code as follows.
```python
import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
```
- Notice how we added a third parameter re.IGNORECASE. Running this program with MALAN@HARVARD.EDU, the input is now considered valid.
- Consider the following email address malan@cs50.harvard.edu. Using our code above, this would be considered invalid. Why might that be?
- Since there is an additional ., the program considers this invalid.

- It turns out that we can, looking at our vocabulary from before, we can group together ideas.
```python
A|B     either A or B
(...)   a group
(?:...) non-capturing version
```
```python
import re

email = input("What's your email? ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")
```
- Notice how the (\w+\.)? communicates to the interpreter that this new expression can be there once or not at all. Hence, both malan@cs50.harvard.edu and malan@harvard.edu are considered valid.


- Interestingly enough, the edits we have done so far to our code do not fully encompass all the checking that could be done to ensure a valid email address. Indeed, here is the full expression that one would have to type to ensure that a valid email is inputted:

```python
^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$
```
- You can learn more in Python’s documentation of re.
https://docs.python.org/3/library/re.html
  
## Cleaning Up User Input

- You should never expect your users to always follow your hopes for clean input. Indeed, users will often violate your intentions as a programmer.

- There are ways to clean up your data.

Normalize names like “**Malan, David**” → “**David Malan**”.

**Step 1 – simple split**
```py
name = input("What's your name? ").strip()
if "," in name:
    last, first = name.split(", ")
    name = f"{first} {last}"
print(f"Hello, {name}")
```

- You might notice that typing in Malan,David with no space causes the interpreter to throw an error. Since we now know some regular expression syntax, let’s apply that to our code:

**Step 2 – with regex groups**
```py
import re
name = input("What's your name? ").strip()
m = re.search(r"^(.+), *(.+)$", name)  # group(1)=last, group(2)=first
if m:
    name = m.group(2) + " " + m.group(1)
print(f"Hello, {name}")
```
- It just so happens that we can request specific groups back using matches.group. 
- Notice the addition of the * in our validation statement. This code will now accept and properly process Malan,David. Further, it will properly handle ` David,Malan with many spaces in front of David`.


- `*` tolerates extra spaces.
- Walrus trick to capture-and-test in one go:
```py
if m := re.search(r"^(.+), *(.+)$", name):
    name = f"{m.group(2)} {m.group(1)}"
```

- It is very common to utilize re.search as we have in the previous examples, where matches is on a line of code after. However, we can combine these statements:



```python
import re
name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")
```

- Notice how we combine two lines of our code. The walrus := operator assigns a value from right to left and allows us to ask a boolean question at the same time. Turn your head sideways and you’ll see why this is called a walrus operator.

- You can learn more in Python’s documentation of re.
https://docs.python.org/3/library/re.html
  
## Extracting User Input

Goal: extract a Twitter **username** from a URL.

**Naive replace**
```py
url = input("URL: ").strip()
username = url.replace("https://twitter.com/", "")
print("Username:", username)
```
- Fails for `http`, `www`, or extra path.


- What if the user simply typed twitter.com instead of including the https:// and the like? You can imagine many scenarios where the user may input or neglect to input parts of the URL that would create strange output by this program. To improve this program, we can code as follows:

```
url = input("URL: ").strip()

username = url.removeprefix("https://twitter.com/")
print(f"Username: {username}")
```
- Notice how we utilize the removeprefix method. This method will remove the beginning of a string.


- Within the re library, there is a method called sub. This method allows us to substitute a pattern with something else.
```python
re.sub(pattern, repl, string, count=0, flags=0)

"""
Notice how pattern refers to the regular expression 
we are looking for. Then, there is a repl string that 
we can replace the pattern with. Finally, 
there is the string that we want to do the substitution on.
"""
```


**Regex substitute**
```py
import re
url = input("URL: ").strip()
username = re.sub(r"^https?://(www\.)?twitter\.com/", "", url, flags=re.IGNORECASE)
print("Username:", username)
```

- Notice how the ^ caret was added to the url. Notice also how the . could be interpreted improperly by the interpreter. Therefore, we escape it using a \ to make it \. For the purpose of tolerating both http and https, we add a ? to the end of https?, making the s optional. Further, to accommodate www we add (www\.)? to our code. Finally, just in case the user decides to leave out the protocol altogether, the http:// or https:// is made optional using (https?://).

```python
import re

url = input("URL: ").strip()

matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print(f"Username:", matches.group(2))
```


- Notice how we are searching for the regular expression above in the string provided by the user. In particular, we are capturing that which appears at the end of the URL using (.+)$ regular expression. Therefore, if the user fails to input a URL without a username, no input will be presented.


**Validated capture**
```py
import re
url = input("URL: ").strip()
if m := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, re.IGNORECASE):
    print("Username:", m.group(1))
```
- `(?:...)` is a **non‑capturing** group.
- `[a-z0-9_]+` = one or more valid handle chars.
- <mark>Best practice:</mark> *validate* and *extract* in the **same** regex when you can.
- Notice that the ?: tells the interpreter it does not have to capture what is in that spot in our regular expression.


- You can learn more in Python’s documentation of re.
  https://docs.python.org/3/library/re.html


## Summing Up

- **Regex basics**: literals, metacharacters, quantifiers, anchors, classes.  
- **Flags**: <mark>re.IGNORECASE</mark>, `re.MULTILINE`, `re.DOTALL`.  
- **Cleaning input** with **capturing groups** and the **walrus operator**.  
- **Extracting structured data** (e.g., usernames) with one precise regex.  

> Keep patterns readable. Use **raw strings**, **anchors**, and prefer **`re.fullmatch`** for whole‑string validation.
