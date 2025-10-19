"""
🎯 The Goal of shirt.py
We need to:
Read two command-line arguments:
sys.argv[1] → input image (a .jpg or .png)
sys.argv[2] → output image (same format)
Check for errors:
wrong number of arguments
wrong file extension
input file missing
input and output extensions don’t match
Open the image with Pillow (Image.open).
Resize and crop the image so it matches the shirt’s size (ImageOps.fit).
Overlay the shirt (Image.paste with a mask).
Save the final image (Image.save).


1️⃣ Importing Modules
sys gives access to command-line arguments.
PIL (Python Imaging Library, installed as Pillow) handles image processing.
Image.open() → read image files
ImageOps.fit() → resize and crop proportionally

2️⃣ Checking Command-Line Arguments
if len(sys.argv) != 3:
    sys.exit("Too few or too many command-line arguments")
Every Python script gets a list sys.argv:
sys.argv[0] → script name (shirt.py)
sys.argv[1] → first argument (input)
sys.argv[2] → second argument (output)
If user doesn’t give exactly 2 arguments → exit with message.
💡 sys.exit() ends the program immediately and can print an error message.

3️⃣ File Validation
Here we:
Use .lower() so case (JPG vs jpg) doesn’t matter.
Use .endswith(tuple) to check for multiple possible endings.
Make sure both input/output are allowed and have same extension.

4️⃣ Opening the Image Safely
try/except
If the file doesn’t exist or can’t open, program exits gracefully.
This avoids the ugly Python traceback.

5️⃣ The Magic of Pillow 🪄 — Overlaying the Shirt
Step A: Fit the image
image = ImageOps.fit(image, shirt.size)
ImageOps.fit resizes and crops the input so that it perfectly fits the shirt dimensions while preserving proportions.
The result matches the exact pixel size of shirt.png.

Step B: Overlay the shirt
image.paste(shirt, shirt)
The second argument (mask) tells Pillow to use shirt.png’s alpha channel (transparency) when pasting.
This means only the visible shirt part overlays; transparent parts stay see-through.
Result → your face appears behind the virtual “I took CS50” shirt 😎.

6️⃣ Save the Final Image
image.save(output_file)
This writes your final composite image (e.g., output.jpg) into your folder.


"""

import sys
from PIL import Image, ImageOps


def main():
    # 1. check arguments
    if len(sys.argv) != 3:
        sys.exit('Too few or too many command-line arguments')

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    # 2. validate extensions
    valid_ext = ('.jpg', '.jpeg', '.png')
    if not input_file.lower().endswith(valid_ext):
        sys.exit('Invalid input file format')
    if not output_file.lower().endswith(valid_ext):
        sys.exit('Invalid output file format')

    # 3. check input and output if they have the same extensions
    if not input_file.split('.')[-1].lower() == output_file.split('.')[-1].lower():
        sys.exit('Input and output have different extensions')

    # 4. open and process the file
    try:
        image = Image.open(input_file)
    except FileNotFoundError:
        sys.exit('Input file does not exits')\

    # 5. algorithms of fit and overlay shirt
    shirt = Image.open('shirt.png')
    # resize and crop input file to match the shirt size
    image = ImageOps.fit(image, shirt.size)
    # overlay the shirt using shirt as mask to keep transparency
    image.paste(shirt, shirt)

    # 6. save
    image.save(output_file)


if __name__ == '__main__':
    main()
