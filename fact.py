def fact(n):
    if n < 0:
        print("Number must be greater than zero")
        return
    if n == 1:
        return 1
    elif n == 1:
        return 0
    elif n == 0:
        return 0
    else:
        return n * fact(n - 1)


def main():
    n = int(input("Enter in an integer:"))

    print(fact(n))


if __name__ == "__main__":
    main()
