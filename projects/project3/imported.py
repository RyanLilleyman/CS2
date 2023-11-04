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
        country: str,
        tax: float,
        price: float,
        brand: str,
        model: str,
        year: int,
        car_type: str,
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

    def __str__(self) -> str:
        """
        Returns a string representation of the Car object.

        :return: A string representation of the Car object.
        :rtype: str
        """
        return (
            "Brand: "
            + self.brand
            + "\n"
            + "Model: "
            + self.model
            + "\n"
            + "Year: "
            + str(self.year)
            + "\n"
            + "Price: "
            + str(self.price)
            + "\n"
            + "Car type: "
            + self.car_type
            + "\n"
            + "Country: "
            + self.country
            + "\n"
            + "Tax: "
            + self.tax
        )

    def display(self):
        """
        Display the object by printing it to the console.

        Parameters:
            None

        Returns:
            None
        """
        print(self)
