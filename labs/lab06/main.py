def get_rainfall():
    rainfall_per_month = []
    for i in range(0, 12):
        s = int(input(f"Enter the total rainfall for the {i+1}th month: "))
        rainfall_per_month.append(s)

    return rainfall_per_month


def total_rainfall(rainfall):
    total = 0
    for i in range(0, len(rainfall)):
        total += rainfall[i]
    return total


def average_rainfall(rainfall):
    total = 0
    for i in range(0, len(rainfall)):
        total += rainfall[i]
    return total / len(rainfall)


def highest_rainfall(rainfall):
    max = 0
    for i in range(0, len(rainfall)):
        if rainfall[i] >= max:
            max = rainfall[i]

    return max


def lowest_rainfall(rainfall):
    min = float("inf")
    for i in range(0, len(rainfall)):
        if rainfall[i] <= min:
            min = rainfall[i]
    return min


def main():
    l = get_rainfall()
    print("The total rainfall is: ", total_rainfall(l))
    print("The average rainfall is: ", average_rainfall(l))
    print("The highest rainfal is: ", highest_rainfall(l))
    print("The lowest rainfall is: ", lowest_rainfall(l))


if __name__ == "__main__":
    main()
