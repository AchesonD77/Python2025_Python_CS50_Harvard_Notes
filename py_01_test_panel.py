def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(a):
    while True:
        try:
            return int(input(a))
        except ValueError:
            pass


main()