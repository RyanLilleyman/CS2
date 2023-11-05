# Project No. 3
# Author: Ryan Lilleyman
# Description: Imported Car Class

from car import Car


class ImportCar(Car):
    """
    A subclass of car representing an imported car.

    Attributes:
        brand (str): The brand of the car.
        model (str): The model of the car.
        year (int): The year the car was manufactured.
        price (float): The price of the car.
        car_type (str): The type of the car.
        country (str): The country of origin.
        tax (float): The tax rate for the car.

    """

    def __init__(
        self,
        brand: str,
        model: str,
        year: int,
        price: float,
        car_type: str,
        country: str,
        tax: float,
    ):
        """
        Initializes a new instance of the class.

        Args:
            country (str): The country of origin for the car.
            tax (float): The tax rate for the car.
            price (float): The price of the car.
            brand (str): The brand of the car.
            model (str): The model of the car.
            year (int): The manufacturing year of the car.
            car_type (str): The type of the car.

        Returns:
            None
        """
        super().__init__(brand, model, year, price, car_type)
        self.__country = country
        self.__tax = tax

    @property
    def country(self):
        """
        Get the value of the `country` property.

        :return: The value of the `country` property.
        """
        return self.__country

    @property
    def tax(self):
        """
        Get the value of the 'tax' property.

        :return: The value of the 'tax' property.
        """
        return self.__tax

    @country.setter
    def country(self, value):
        """
        Setter function for the 'country' attribute.

        Args:
            value (str): The value to set for the 'country' attribute.

        Returns:
            None
        """
        self.__country = value

    @tax.setter
    def tax(self, value):
        """
        Set the tax value.

        Parameters:
            value (any): The new tax value.

        Returns:
            None
        """
        self.__tax = value

    def raise_tax_by_five(self):
        """
        Raises the tax rate by 5%.
        """
        self.tax += 5

    def __str__(self) -> str:
        """
        Returns a string representation of the Car object.

        :return: A string representation of the Car object.
        :rtype: str
        """
        formatted_price = "${:,.2f}".format(self.price)
        formatted_tax = "{:,.0f}".format(self.tax)
        return (
            self.brand
            + " "
            + self.model
            + " "
            + str(self.year)
            + " "
            + formatted_price
            + " "
            + self.car_type
            + " "
            + self.country
            + " "
            + formatted_tax
            + "%"
        )

    def print_info(self):
        """
        Display the object by printing it to the console.

        Parameters:
            None

        Returns:
            None
        """
        print(self)
