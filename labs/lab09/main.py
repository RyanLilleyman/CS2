# Import random and time modules
import random
import time


# Define a function to generate a random sorted list of numbers
def generate_list(n):
    # Create an empty list
    lst = []
    # Loop n times
    for i in range(n):
        # Generate a random number between 0 and 100
        num = random.randint(0, 100)
        # Append the number to the list
        lst.append(num)
    # Sort the list in ascending order
    lst.sort()
    # Return the list
    return lst


# Define a function to perform linear search
def linear_search(lst, target):
    iterations = 0
    # Implement Linear Search
    for i, value in enumerate(lst):
        if value == target:
            return i, iterations
        iterations += 1
    return -1, iterations


# Define a function to perform binary search
def binary_search(lst, target):
    # Initialize the number of iterations to 0
    iterations = 0
    # Implement Binary Search
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid, iterations
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        iterations += 1

    return -1, iterations


# Generate a random sorted list of 10 numbers
lst = generate_list(10)
# Print the list
print("The list is:", lst)
# Choose a random target value from the list
target = random.choice(lst)
# Print the target value
print("The target value is:", target)
print()

# Perform linear search and measure the time
start = time.time()
index, iterations = linear_search(lst, target)
end = time.time()
# Print the results of linear search
print("Linear search:")
print("Index:", index)
print("Iterations:", iterations)
print("Time:", end - start)
print()

# Perform binary search and measure the time
start = time.time()
index, iterations = binary_search(lst, target)
end = time.time()
# Print the results of binary search
print("Binary search:")
print("Index:", index)
print("Iterations:", iterations)
print("Time:", end - start)
