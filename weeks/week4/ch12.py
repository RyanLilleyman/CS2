# This program has a recursive function.

def main():
    message()

def message():
    print('This is a recursive function.')
    message()

# Call the main function.
main()

#############################################

# This program has a recursive function.

def main():
    # By passing the argument 5 to the message
    # function we are telling it to display the
    # message five times.
    message(5)

def message(times):
    if times > 0:
        print('This is a recursive function.')
        message(times - 1)

# Call the main function.
main()

############################################

# This program uses recursion to calculate
# the factorial of a number.

def main():
    # Get a number from the user.
    number = int(input('Enter a nonnegative integer: '))

    # Get the factorial of the number.
    fact = factorial(number)

    # Display the factorial.
    print('The factorial of', number, 'is', fact)

# The factorial function uses recursion to
# calculate the factorial of its argument,
# which is assumed to be nonnegative.
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

# Call the main function.
main()

############################################

# This program demonstrates the range_sum function.

def main():
    # Create a list of numbers.
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Get the sum of the items at indexes 2
    # through 5.
    my_sum = range_sum(numbers, 2, 5)

    # Display the sum.
    print('The sum of items 2 through 5 is', my_sum)

# The range_sum function returns the sum of a specified
# range of items in num_list. The start parameter
# specifies the index of the starting item. The end
# parameter specifies the index of the ending item.
def range_sum(num_list, start, end):
    if start > end:
        return 0
    else:
        return num_list[start] + range_sum(num_list, start + 1, end)

# Call the main function.
main()

##############################################

# This program uses recursion to print numbers
# from the Fibonacci series.

def main():
    print('The first 10 numbers in the')
    print('Fibonacci series are:')

    for number in range(1, 11):
        print(fib(number))

# The fib function returns the nth number
# in the Fibonacci series.
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# Call the main function.
main()

##############################################

# This program uses recursion to find the GCD
# of two numbers.

def main():
    # Get two numbers.
    num1 = int(input('Enter an integer: '))
    num2 = int(input('Enter another integer: '))

    # Display the GCD.
    print('The greatest common divisor of')
    print('the two numbers is', gcd(num1, num2))

# The gcd function returns the greatest common
# divisor of two numbers.
def gcd(x, y):
    if x % y == 0:
        return y
    else:
        return gcd(x, x % y)

# Call the main function.
main()

##############################################

# This program simulates the Towers of Hanoi game.

def main():
    # Set up some initial values.
    num_discs = 3
    from_peg = 1
    to_peg = 3
    temp_peg =2

    # Play the game.
    move_discs(num_discs, from_peg, to_peg, temp_peg)
    print('All the pegs are moved!')

# The moveDiscs function displays a disc move in
# the Towers of Hanoi game.
# The parameters are:
#    num:      The number of discs to move.
#    from_peg: The peg to move from.
#    to_peg:   The peg to move to.
#    temp_peg: The temporary peg.
def move_discs(num, from_peg, to_peg, temp_peg):
    if num > 0:
        move_discs(num - 1, from_peg, temp_peg, to_peg)
        print('Move a disc from peg', from_peg, 'to peg', to_peg)
        move_discs(num - 1, temp_peg, to_peg, from_peg)

# Call the main function.
main()
