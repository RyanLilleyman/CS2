def main():
    n = int(input("Enter the number of lines."))
    printLines(n)


def printLines(n):
    if n == 1:
        print("*")
    else:
        printLines(n - 1)
        print("*" * n)


if __name__ == "__main__":
    main()
