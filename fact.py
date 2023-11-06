def fib(n):
    """
    Calculates the nth Fibonacci number.

    Args:
        n (int): The index of the Fibonacci number to calculate.

    Returns:
        int: The nth Fibonacci number.
    """
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 0:
        return 0
    else:
        return fib(n - 2) + fib(n - 1)


def fact(n):
    """
    Calculate the factorial of a given number.

    Parameters:
        n (int): The number whose factorial is to be calculated.

    Returns:
        int: The factorial of the given number.
    """
    if n == 1:
        return 1
    if n == 0:
        return 0
    else:
        return n * fact(n - 1)


def isPrime(n: int, i: int = 2) -> bool:
    """
    Check if a given number is prime.

    Parameters:
        n (int): The number to check.
        i (int, optional): The starting number for iteration. Defaults to 2.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if i < n and n % i == 0:
        return False
    if n % i == 0:
        return True
    else:
        return isPrime(n, i + 1)


def main():
    """
    Executes the main logic of the program.

    This function prompts the user to enter a number, calculates and prints the Fibonacci number,
    the factorial, and checks if the number is prime. The function does not take any parameters
    and does not return any values.

    Parameters:
        None

    Returns:
        None
    """
    n = int(input("Enter a number: "))
    print(fib(n))
    print(fact(n))
    print(isPrime(n))


if __name__ == "__main__":
    main()
