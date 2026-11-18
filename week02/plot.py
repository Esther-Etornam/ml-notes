def area(length, width):
    return length * width


def main():
    length = int(input("Enter length in metres: "))
    width = int(input("Enter width in metres: "))

    result = area(length, width)

    print(f"Area: {result} square metres")


main()