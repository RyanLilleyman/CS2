"""
PMT #2
By Ryan Lilleyman
Date: November 28th, 2023
"""
from vehicle import Vehicle


class Deluxe(Vehicle):
    """
    Deluxe class inherits from Vehicle
    """

    def __init__(self, brand, vin, mileage):
        """
        Initializes a new instance of the DeluxeCar class.

        Parameters:
            brand (str): The brand of the car.
            vin (str): The vehicle identification number (VIN) of the car.
            mileage (float): The mileage of the car.

        Returns:
            None
        """
        super().__init__(brand, vin, mileage)
        self.type = "Deluxe"

    def get_lease_amount(self):
        """
        Calculates and returns the lease amount for the vehicle.

        This function multiplies 12 by 520 and adds the product to the product of the vehicle's mileage and 0.1.

        Returns:
            float: The calculated lease amount.
        """
        return (12 * 520) + (self.get_mileage() * 0.1)

    def get_type(self):
        """
        Get the type of the object.

        :return: The type of the object.
        """
        return self.type
