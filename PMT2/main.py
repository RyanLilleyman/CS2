"""
PMT #2
By Ryan Lilleyman
Date: November 28th, 2023
"""
from luxury import Luxury
from deluxe import Deluxe
from royalty import Royalty
from customer import Customer


def main():
    """
    Executes the main logic of the program.

    This function creates a Customer object and initializes three Vehicle objects: Royalty, Luxury, and Deluxe.
    It adds these vehicles to the customer's list of vehicles using the `add_vehicle` method.
    The function then retrieves the list of vehicles using the `get_vehicles` method.
    It prints a header for the vehicle lease expenses and formats the table.
    It iterates over the vehicles list and prints the vehicle type, brand, VIN, and lease amount.
    After printing the vehicles, it calculates and prints the total vehicle lease amount using the `calculate_total_lease` method.
    It then adds two more vehicles to the customer's list and repeats the process of printing the vehicles and calculating the total lease amount.

    Parameters:
    None

    Returns:
    None
    """
    cust = Customer()
    vehicle1 = Royalty("Limousine", "VZT2002357", 150)  # (brand, vin, mileage)
    vehicle2 = Luxury("Lamborghini", "VGH2005649", 200)  # (brand, vin, mileage)
    vehicle3 = Deluxe("Lexus", "VQP2005963", 200)  # (brand, vin, mileage)
    cust.add_vehicle(vehicle1)
    cust.add_vehicle(vehicle2)
    cust.add_vehicle(vehicle3)
    vehicles = cust.get_vehicles()
    print("Vehicle Lease Expenses")
    print("======================\n")
    print(f'{"Vehicle Type":<15}{"Brand":<15}' f'{"VIN":<12}' f'{"Lease Amount":>10}')
    print(f'{"------------":<15}{"-----":<15}' f'{"---":<12}' f'{"------------":>10}')
    for i in range(len(vehicles)):
        print(
            f"{vehicles[i].get_type():<15}{vehicles[i].get_brand():<15}"
            f"{vehicles[i].get_vin():<12}"
            f'{"$"}{vehicles[i].get_lease_amount():>10,.2f}'
        )
    print()
    print(f'{"Total vehicle lease amount: $"}{cust.calculate_total_lease():>10,.2f}')
    vehicle4 = Royalty("Rolls-Royce", "VPL2006637", 200)  # (brand, vin, mileage)
    vehicle5 = Deluxe("Camry", "VVV2006415", 250)  # (brand, vin, mileage)
    cust.add_vehicle(vehicle4)
    cust.add_vehicle(vehicle5)
    print()
    for i in range(len(vehicles)):
        print(
            f"{vehicles[i].get_type():<15}{vehicles[i].get_brand():<15}"
            f"{vehicles[i].get_vin():<12}"
            f'{"$"}{vehicles[i].get_lease_amount():>10,.2f}'
        )
    print()
    print(f'{"Total vehicle lease amount: $"}{cust.calculate_total_lease():>10,.2f}')


if __name__ == "__main__":
    main()
