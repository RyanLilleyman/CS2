"""
PMT #2
By Ryan Lilleyman
Date: November 28th, 2023
"""
from vehicle import Vehicle


class Royalty(Vehicle):
    """
    Royalty class inherits from Vehicle
    """

    def __init__(self, brand, vin, mileage):
        """
        Initializes a new instance of the RoyaltyCar class.

        Parameters:
            brand (str): The brand of the car.
            vin (str): The VIN (Vehicle Identification Number) of the car.
            mileage (float): The mileage of the car.

        Returns:
            None
        """
        super().__init__(brand, vin, mileage)
        self.type = "Royalty"

    def get_lease_amount(self):
        """
        Calculates and returns the lease amount for the vehicle.

        Returns:
            float: The calculated lease amount.
        """
        return (12 * 1050) + (self.get_mileage() * 0.2)

    def get_type(self):
        """
        Get the type of the object.

        Returns:
            The type of the object.
        """
        return self.type
