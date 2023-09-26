def toRaise(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    else:
        return x * toRaise(x, n - 1)


def main():
    x = int(input("Enter the number to be raised: "))
    n = int(input("Enter the exponent: "))
    print(toRaise(x, n))


if __name__ == "__main__":
    main()
