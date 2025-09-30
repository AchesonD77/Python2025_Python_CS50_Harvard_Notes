# int()
# Converts a string to an integer.

#Variables
# We’ll store:
# m = mass (input from user)
# c = 300000000 (speed of light, constant)
# E = m * c ** 2

# Exponentiation **
# In Python: 2 ** 3  # means 2^3 = 8

def main():
    m = int(input("m: "))

    C = 300000000

    E = m * C ** 2

    print(E)


main()


# m = int(input("m: "))
# c = 300000000
# E = m * c ** 2
# print(E)