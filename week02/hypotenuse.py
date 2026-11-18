def square(n):
    return n ** 2


def sum_of_squares(a, b):
    return square(a) + square(b)


def hypotenuse(a, b):
    return sum_of_squares(a, b) ** 0.5


def main():
    a = float(input("Enter first side: "))
    b = float(input("Enter second side: "))

    result = hypotenuse(a, b)

    print(f"Hypotenuse: {result}")


if __name__ == "__main__":
    main()