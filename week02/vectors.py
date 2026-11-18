# Exercise 1: Dot product of two 2D vectors

def dot2(a1, a2, b1, b2):
    return (a1 * b1) + (a2 * b2)


# Exercise 2: Dot product of two 3D vectors

def dot3(a1, a2, a3, b1, b2, b3):
    return (a1 * b1) + (a2 * b2) + (a3 * b3)


# Exercise 3: Length of a 2D vector

def length2(x, y):
    return dot2(x, y, x, y) ** 0.5


# Exercise 4: Basket total

def basket(q1, q2, q3, p1, p2, p3):
    return (q1 * p1) + (q2 * p2) + (q3 * p3)


# Main function

def main():
    print("Dot product 2D:", dot2(1, 2, 3, 5))

    print("Dot product 3D:", dot3(1, 0, 2, 4, 5, 6))

    print("Vector length:", length2(6, 8))

    print("Basket total:", basket(3, 2, 5, 5, 12, 1))


if __name__ == "__main__":
    main()