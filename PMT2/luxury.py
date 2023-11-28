"""
PMT #2
By Ryan Lilleyman
Date: November 28th, 2023
"""
from vehicle import Vehicle


class Luxury(Vehicle):
    """
    Luxury class inherits from Vehicle
    """

    def __init__(self, brand, vin, mileage):
        """
        Initializes a new instance of the LuxuryCar class.

        Parameters:
            brand (str): The brand of the luxury car.
            vin (str): The VIN (Vehicle Identification Number) of the luxury car.
            mileage (float): The mileage of the luxury car.

        Returns:
            None
        """
        super().__init__(brand, vin, mileage)
        self.type = "Luxury"

    def get_lease_amount(self):
        """
        Calculate and return the lease amount based on the number of months (12) and the monthly payment (835),
        as well as the mileage of the vehicle multiplied by the mileage rate (0.15).

        Parameters:
        - None

        Returns:
        - The lease amount as a float.
        """
        return (12 * 835) + (self.get_mileage() * 0.15)

    def get_type(self):
        """
        Get the type of the object.
        """
        return self.type
