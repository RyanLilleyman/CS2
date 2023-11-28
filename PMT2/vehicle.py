"""
PMT #2
By Ryan Lilleyman
Date: November 28th, 2023
"""


class Vehicle:
    """
    Main Vehicle Superclass
    """

    def __init__(self, brand, vin, mileage):
        """
        Initializes a new instance of the class.

        Parameters:
            brand (str): The brand of the vehicle.
            vin (str): The vehicle identification number.
            mileage (float): The mileage of the vehicle.

        Returns:
            None
        """
        self.brand = brand
        self.vin = vin
        self.mileage = mileage

    def get_brand(self):
        """
        Returns the brand of the object.
        """
        return self.brand

    def get_vin(self):
        """
        Get the VIN of the object.

        Returns:
            str: The VIN of the object.
        """
        return self.vin

    def get_mileage(self):
        """
        Returns the mileage of the object.

        :param self: The object.
        :return: The mileage of the object.
        """
        return self.mileage

    def get_lease_amount(self):
        """
        Get the lease amount.
        """
        pass
