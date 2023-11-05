# Project No. 3
# Author: Ryan Lilleyman
# Description: def main():

import os
from imported import ImportCar
from domestic import DomesticCar


def get_script_directory():
    """
    Return the directory of the script.

    Returns:
        str: The absolute path of the directory containing the script.

    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return script_dir


def check_file_in_script_dir(script_dir: str, file: str):
    """
    Check if a file exists in the specified script directory.

    Args:
        script_dir (str): The directory where the file is located.
        file (str): The name of the file.

    Returns:
        bool: True if the file exists, False otherwise.
    """
    temp_file = os.path.join(script_dir, file)
    return os.path.exists(temp_file)


def step_one():
    """
    This function performs the first step of a multi-step process.

    It prompts the user to enter a file name that contains information about cars in stock.

    The function then checks if the file exists in the script directory. If the file is found, it opens the file and reads its contents.

    The function parses the file and creates lists of imported and domestic cars based on the information in the file.

    It then prints the information of each imported and domestic car separately.

    Finally, the function calculates and prints the total number of imported and domestic cars.

    Parameters:
        No parameters.

    Returns:
        A tuple containing two lists: imported_cars and domestic_cars. Each list contains objects representing the cars and their information.
    """
    print("Step One:", end="\n\n")
    while True:
        f = str(
            input("Please enter a file name (with information about Cars in Stock): ")
        )
        print()
        if check_file_in_script_dir(get_script_directory(), f):
            break
        else:
            print("File not Found.")
            continue

    f = os.path.join(get_script_directory(), f)
    with open(f, "r+", encoding="utf-8") as file:
        lines = [line.strip().split(" ") for line in file.readlines()]
        imported_cars = [
            ImportCar(
                line[1],
                line[2],
                int(line[3]),
                float(line[4]),
                line[5],
                line[6],
                float(line[7]),
            )
            for line in lines
            if line[0] == "I"
        ]
        domestic_cars = [
            DomesticCar(
                line[1], line[2], int(line[3]), float(line[4]), line[5], line[6]
            )
            for line in lines
            if line[0] == "D"
        ]

        print("Imported Cars: ", end="\n\n")
        for car in imported_cars:
            car.print_info()
        print()
        print("Domestic Cars: ", end="\n\n")
        for car in domestic_cars:
            car.print_info()
        print()
        print("Number of imported cars = ", len(imported_cars))
        print("Number of domestic cars = ", len(domestic_cars))
        print("Total = ", len(imported_cars) + len(domestic_cars))
        to_return = (imported_cars, domestic_cars)

    return to_return


def step_two():
    """
    This function performs step two of a larger process. It retrieves the current inventory by calling the `step_one()` function. It then prompts the user to enter a file name that contains information about cars expected to arrive. The file must be named "carsExpectedToArrive.txt". If the file is found in the script directory, the function reads the file and extracts data about imported cars and domestic cars. The imported cars are stored in a list of `ImportCar` objects, and the domestic cars are stored in a list of `DomesticCar` objects. The function then updates the current inventory by adding the imported cars and domestic cars to the respective lists. After updating the inventory, the function prints the information of all imported cars and domestic cars, along with the total number of imported cars and domestic cars. Finally, the function returns the updated inventory.

    Parameters:
    None

    Return type:
    list
        - A list containing two lists: the first list represents the imported cars, and the second list represents the domestic cars.
    """
    current_inventory = step_one()
    print()
    print("Step Two:", end="\n\n")
    while True:
        f = str(
            input(
                "Please enter a file name (with information about Cars expected to arrive): "
            )
        )
        print()
        if f == "carsExpectedToArrive.txt":
            if check_file_in_script_dir(get_script_directory(), f):
                break
            else:
                print("File not Found.")
                continue
        else:
            print("File must me named carsExpectedToArrive.txt.")

    f = os.path.join(get_script_directory(), f)
    with open(f, "r+", encoding="utf-8") as file:
        lines = [line.strip().split(" ") for line in file.readlines()]
        imported_cars_arrive = [
            ImportCar(
                line[1],
                line[2],
                int(line[3]),
                float(line[4]),
                line[5],
                line[6],
                float(line[7]),
            )
            for line in lines
            if line[0] == "I"
        ]
        domestic_cars_arrive = [
            DomesticCar(
                line[1], line[2], int(line[3]), float(line[4]), line[5], line[6]
            )
            for line in lines
            if line[0] == "D"
        ]

        current_imported = current_inventory[0]
        current_domestic = current_inventory[1]

        current_imported.extend(imported_cars_arrive)
        current_domestic.extend(domestic_cars_arrive)

        print("Imported Cars: ", end="\n\n")
        for car in current_inventory[0]:
            car.print_info()
        print()
        print("Domestic Cars: ", end="\n\n")
        for car in current_inventory[1]:
            car.print_info()
        print()
        print("Number of imported cars = ", len(current_inventory[0]))
        print("Number of domestic cars = ", len(current_inventory[1]))
        print("Total = ", len(current_inventory[0]) + len(current_inventory[1]))

    return current_inventory


def step_three(current_inventory):
    """
    Perform step three of the inventory management process.

    Args:
        current_inventory (list): A list containing two sublists representing the current inventory. The first sublist contains imported cars and the second sublist contains domestic cars.

    Returns:
        None
    """
    print()
    print("Step Three: ", end="\n\n")
    print("Imported Cars: ", end="\n\n")
    for car in current_inventory[0]:
        car.raise_tax_by_five()
        car.print_info()
    print()
    print("Domestic Cars: ", end="\n\n")
    for car in current_inventory[1]:
        car.raise_price_by_fifteen_percent()
        car.print_info()
    print()
    print("Number of imported cars = ", len(current_inventory[0]))
    print("Number of domestic cars = ", len(current_inventory[1]))
    print("Total = ", len(current_inventory[0]) + len(current_inventory[1]))


def step_four(current_inventory):
    """
    Generates a filtered list of cars from the given current_inventory based on a maximum price threshold of 15000.

    Args:
        current_inventory (list): A list containing two sublists representing the current inventory of cars. Each sublist contains Car objects.

    Returns:
        None
    """
    print()
    print("Step Four: ", end="\n\n")
    print("Filter price less than or equal to: ", 15000)

    newli = []
    total = 0

    for car in current_inventory[0]:
        if car.price <= 15000:
            newli.append(car)

    for car in current_inventory[1]:
        if car.price <= 15000:
            newli.append(car)

    newli.sort(key=lambda x: x.price)
    for car in newli:
        car.print_info()

    print()
    print("Number of cars = ", len(newli), end="\n\n")

    for car in current_inventory[0]:
        total += car.price
    for car in current_inventory[1]:
        total += car.price
    print("Total price of cars in the Stock: ", total)


def main():
    """
    The main function of the program.
    """
    print("Welcome to the Domestic/Imported Cars Application", end="\n\n")
    current_inventory = step_two()

    step_three(current_inventory)
    step_four(current_inventory)


if __name__ == "__main__":
    main()
