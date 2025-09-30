'''
Task
Write a program in extensions.py that:
Asks the user for a file name.
Looks at the file extension (e.g., .jpg, .pdf, etc.).
Outputs the correct MIME type.
If the extension is unknown or missing → output application/octet-stream.


.strip()
Removes spaces around input.

.lower()
Makes everything lowercase → so .JPG and .jpg are treated the same.

.endswith()
Checks if a string ends with a suffix.


Why .strip().lower()?
.strip() → removes extra spaces (like " file.pdf ").
.lower() → makes extension comparison case-insensitive (.JPG = .jpg).

Why .endswith()?
Safer than slicing (filename[-4:]) because extensions have different lengths (.gif vs .jpeg).
.endswith() works regardless of length.

Default Case
If the extension isn’t recognized → fallback to:
'''


def file_extensions():
    filename = input("File name: ").strip().lower()

    if filename.endswith(".gif"):
        print("image/gif")
    elif filename.endswith((".jpg")) or filename.endswith(".jpeg"):
        print("image/jpeg")
    elif filename.endswith(".png"):
        print("image/png")
    elif filename.endswith('.pdf'):
        print('application/pdf')
    elif filename.endswith('.txt'):
        print('text/plain')
    elif filename.endswith('.zip'):
        print('application/zip')
    else:
        print('application/octet-stream')


file_extensions()