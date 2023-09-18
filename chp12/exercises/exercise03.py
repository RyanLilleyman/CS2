def main():
    n = int(input("Enter the number of lines."))
    printLines(n)


def printLines(n):
    print("*" * (n - (n - 1)))
    if n == 1:
        return print("*")
    return printLines(n - 1)


if __name__ == "__main__":
    main()
