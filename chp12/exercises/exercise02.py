def main():
    n, y = int(input("Enter first integer to multiply.")), int(
        input("Enter second integer to multiply.")
    )

    print(mult(n, y))


def mult(n, y):
    if n == 1:
        return y
    return y + mult(n - 1, y)


if __name__ == "__main__":
    main()
