def main():
    n = int(input("Enter an integer: "))
    printInteger(n)


def printInteger(n):
    print(n)
    if n == 0:
        return
    return printInteger(n - 1)


if __name__ == "__main__":
    main()
