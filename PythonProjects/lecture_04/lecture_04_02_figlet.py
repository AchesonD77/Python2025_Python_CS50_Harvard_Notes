"""
learn about command-line arguments, modules, error handling, and ASCII art generation using the pyfiglet library.

You will write figlet.py, a Python program that:
Accepts zero or two command-line arguments:
Zero → use a random font
Two → specify a font (with -f or --font fontname)
Prompts the user for a string of text.
Prints the text as ASCII art using that font.

Step 1. Install the Required Library
You’ll need the external library pyfiglet (a Python version of the old-school FIGlet program).
Install it with:
pip install pyfiglet

Step 2. Understand the Tools
Tool	Purpose
sys.argv	Lets us access command-line arguments
pyfiglet.Figlet()	Creates a “font engine” object
Figlet.getFonts()	Returns a list of all available fonts
Figlet.setFont(font=...)	Chooses a specific font
sys.exit()	Ends the program immediately with an error message


1. import sys, random, from pyfiglet import Figlet
sys → used for command-line arguments.
random → for choosing a random font when no argument is given.
pyfiglet.Figlet() → main class that generates ASCII art.

2. figlet = Figlet()
This creates a Figlet object, which can:
store available fonts (.getFonts())
render text (.renderText())

3. fonts = figlet.getFonts()
This returns a Python list of all available font names (hundreds of them!).
For example:
['slant', 'standard', '3-d', 'digital', 'isometric1', ...]

4. Handling Command-Line Arguments
Python stores arguments in a list called sys.argv.
Example:
python figlet.py -f slant
Then:
sys.argv == ['figlet.py', '-f', 'slant']
So:
sys.argv[0] = program name
sys.argv[1] = -f
sys.argv[2] = slant

5. The Conditions
if len(sys.argv) == 1:
    # No arguments → random font
elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
    # Valid input → set specific font
else:
    # Wrong input → exit

Otherwise, the program exits safely using:
sys.exit("Usage: figlet.py [-f FONT]")

6. Random Font Logic
If the user doesn’t specify a font:
font = random.choice(fonts)
figlet.setFont(font=font)
→ Picks a random font from the list.

7. Render Text
text = input("Input: ")
print(figlet.renderText(text))
The renderText() method turns your text into ASCII art.


"""

import random
import sys
from pyfiglet import Figlet


def main():
    figlet = Figlet()
    fonts = figlet.getFonts()

    # no argument: using random fonts
    if len(sys.argv) == 1:
        font = random.choice(fonts)
        figlet.setFont(font = font)

    # if 2 arguments:
    elif len(sys.argv) == 3 and sys.argv[1] in ['-f', '--font']:
        font = sys.argv[2]
        if font not in fonts:
            sys.exit("Invalid font name.")
        figlet.setFont(font = font)

    # if wrong number of arguments: exit
    else:
        sys.exit("Usage: figlet.py [-f FONT]")

    # get input from user
    text = input("Input: ")
    print("Output: ")
    print(figlet.renderText(text))


if __name__ == '__main__':
    main()