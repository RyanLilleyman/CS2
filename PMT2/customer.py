"""
PMT #2
By Ryan Lilleyman
Date: November 28th, 2023
"""


class Customer:
    """
    Customer class
    """

    def __init__(self):
        """
        Initializes the class instance by creating an empty list to store vehicles.

        Parameters:
        None

        Returns:
        None
        """
        self.vehicles = []

    def get_vehicles(self):
        """
        Get the vehicles.
        """
        return self.vehicles

    def add_vehicle(self, vehicle):
        """
        Add a vehicle to the list of vehicles.

        Parameters:
            vehicle (Vehicle): The vehicle object to be added.

        Returns:
            None
        """
        self.vehicles.append(vehicle)

    def calculate_total_lease(self):
        """
        Calculate the total lease amount for all vehicles.

        Returns:
            The total lease amount (float).
        """
        return sum([item.get_lease_amount() for item in self.vehicles])
