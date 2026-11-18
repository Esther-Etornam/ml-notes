def square(n):
    return n ** 2


def sum_of_squares(a, b):
    return square(a) + square(b)


def main():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = sum_of_squares(a, b)

    print(f"Result: {result}")


if __name__ == "__main__":
    main()