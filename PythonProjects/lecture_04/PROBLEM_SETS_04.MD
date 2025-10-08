# 1. Emojize
- Because emoji aren’t quite as easy to type as text, at least on laptops and desktops, some programs support “codes,” whereby you can type, for instance, :thumbs_up:, which will be automatically converted to 👍. Some programs additionally support aliases, whereby you can more succinctly type, for instance, :thumbsup:, which will also be automatically converted to 👍.

- See carpedm20.github.io/emoji/all.html?enableList=enable_list_alias for a list of codes with aliases.

- In a file called emojize.py, implement a program that prompts the user for a str in English and then outputs the “emojized” version of that str, converting any codes (or aliases) therein to their corresponding emoji.

# 2.Frank, Ian and Glen’s Letters
- FIGlet, named after Frank, Ian, and Glen’s letters, is a program from the early 1990s for making large letters out of ordinary text, a form of ASCII art:
```
 _ _ _          _   _     _
| (_) | _____  | |_| |__ (_)___
| | | |/ / _ \ | __| '_ \| / __|
| | |   <  __/ | |_| | | | \__ \
|_|_|_|\_\___|  \__|_| |_|_|___/
```

- Among the fonts supported by FIGlet are those at figlet.org/examples.html.

- FIGlet has since been ported to Python as a module called pyfiglet.

- In a file called figlet.py, implement a program that:

- Expects zero or two command-line arguments:
    - Zero if the user would like to output text in a random font.
  - Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
  
- Prompts the user for a str of text.
- Outputs that text in the desired font.
- If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.

# 3. Adieu
- In The Sound of Music, there’s a song sung largely in English, So Long, Farewell, with these lyrics, wherein “adieu” means “goodbye” in French:

- Adieu, adieu, to yieu and yieu and yieu

- Of course, the line isn’t grammatically correct, since it would typically be written (with an Oxford comma) as:

- Adieu, adieu, to yieu, yieu, and yieu

- To be fair, “yieu” isn’t even a word; it just rhymes with “you”!

- In a file called adieu.py, implement a program that prompts the user for names, one per line, until the user inputs control-d. Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one and, three names with two commas and one and, and 𝑛 names with 𝑛 −1 commas and one and, as in the below:
```
Adieu, adieu, to Liesl
Adieu, adieu, to Liesl and Friedrich
Adieu, adieu, to Liesl, Friedrich, and Louisa
Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl
```

# 4. Guessing Game
- I’m thinking of a number between 1 and 100…

- What is it?
- In a file called game.py, implement a program that:

- Prompts the user for a level, 𝑛. If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and 𝑛, inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
```If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
If the guess is larger than that integer, the program should output Too large! and prompt the user again.
If the guess is the same as that integer, the program should output Just right! and exit.
  ```

# 5. Little professor 
- One of David’s first toys as a child, funny enough, was Little Professor, a “calculator” that would generate ten different math problems for David to solve. For instance, if the toy were to display 4 + 0 = , David would (hopefully) answer with 4. If the toy were to display 4 + 1 = , David would (hopefully) answer with 5. If David were to answer incorrectly, the toy would display EEE. And after three incorrect answers for the same problem, the toy would simply display the correct answer (e.g., 4 + 0 = 4 or 4 + 1 = 5).

- In a file called professor.py, implement a program that:

- Prompts the user for a level, 𝑛. If the user does not input 1, 2, or 3, the program should prompt again.
Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with 𝑛 digits. No need to support operations other than addition (+).
Note: The order in which you generate x and y matters. Your program should generate random numbers in x, y pairs to simulate generating one math question at a time (e.g., x0 with y0, x1 with y1, and so on).

- Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries, the program should output the correct answer.
The program should ultimately output the user’s score: the number of correct answers out of 10.
Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, and generate_integer returns a single randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:
```
import random


def main():
    ...


def get_level():
    ...


def generate_integer(level):
    ...


if __name__ == "__main__":
    main()
```

# 6. Bitcoin Price Index
- As of Saturday, April 5, 2025 at 3:00 PM GMT+2, we are aware of the CoinCap v2 API deprecation that may affect students’ ability to complete this problem. We have now updated the problem to use the CoinCap v3 API instead. If you have already started working on this problem, you must update your code to use the CoinCap v3 API instead of the CoinCap v2 API. Importantly, you will need to sign up for a CoinCap account and obtain an API key. You can do this by visiting CoinCap. Once you have your API key, you can use it in your code to access the CoinCap v3 API.

- Bitcoin is a form of digital currency, otherwise known as cryptocurrency. Rather than rely on a central authority like a bank, Bitcoin instead relies on a distributed network, otherwise known as a blockchain, to record transactions.

- Because there’s demand for Bitcoin (i.e., users want it), users are willing to buy it, as by exchanging one currency (e.g., USD) for Bitcoin.

- In a file called bitcoin.py, implement a program that:

- Expects the user to specify as a command-line argument the number of Bitcoins, 𝑛, that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
- Queries the API for the CoinCap Bitcoin Price Index at rest.coincap.io/v3/assets/bitcoin?apiKey=YourApiKey. You should replace YourApiKey with the actual API key you obtained from your CoinCap account dashboard, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions, as with code like:
```
import requests

try:
    ...
except requests.RequestException:
    ...
   ```
- Outputs the current cost of 𝑛 Bitcoins in USD to four decimal places, using , as a thousands separator.