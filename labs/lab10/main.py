import time
import random


def generate_list(n):
    lst = []
    for i in range(n):
        num = random.randint(0, 100)
        lst.append(num)
    return lst


def bubbleSort(array):
    for i in range(len(array)):
        swapped = False
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

                swapped = True
        if not swapped:
            break


def selectionSort(array):
    for step, _ in enumerate(array):
        min_idx = step

        for i in range(step + 1, len(array)):
            if array[i] < array[min_idx]:
                min_idx = i

        (array[step], array[min_idx]) = (array[min_idx], array[step])


def main():
    lst = generate_list(100)
    print("The list is:", lst)
    tmp = lst
    print()

    start = time.time()
    selectionSort(lst)
    end = time.time()

    print("Selection sort:", end="\n\n")
    print("Time: ", end - start, end="\n\n")

    start = time.time()
    bubbleSort(tmp)
    end = time.time()
    print()
    print("Bubble sort:", end="\n\n")
    print("Time: ", end - start, end="\n\n")


if __name__ == "__main__":
    main()
