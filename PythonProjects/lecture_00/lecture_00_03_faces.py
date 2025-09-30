# We already know the string method .replace() from the last exercise.
# Here we just need two replacements:

def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text


def main():
    print(convert(input("")))

main()

# Functions help you reuse code and organize programs.
# Here, convert handles text conversion, while main handles program flow.
