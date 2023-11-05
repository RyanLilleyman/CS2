# Project No. 3
# Author: Ryan Lilleyman
# Description: Domestic car subclass.

from car import Car


class DomesticCar(Car):
    """
    A subclass of car representing a domestic car.

    Attributes:
        brand (str): The brand of the car.
        model (str): The model of the car.
        year (int): The year the car was manufactured.
        price (float): The price of the car.
        car_type (str): The type of the car.
        state (str): The state where the car comes from.

    """

    def __init__(
        self,
        brand: str,
        model: str,
        year: int,
        price: float,
        car_type: str,
        state: str,
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
        self.__state = state

    @property
    def state(self):
        """
        Get the value of the 'state' property.

        Returns:
            The value of the 'state' property.
        """
        return self.__state

    @state.setter
    def state(self, value):
        """
        Setter method for the 'state' attribute.

        Args:
            value: The new value to set for the 'state' attribute.

        Returns:
            None
        """
        self.__state = value

    def raise_price_by_fifteen_percent(self):
        """
        Raises the price of the object by fifteen percent.

        This method multiplies the current price of the object by 1.15, effectively increasing it by fifteen percent.

        Parameters:
        - self: The object on which the method is called.

        Returns:
        - None: This method does not return any value.
        """
        self.price *= 1.15

    def __str__(self) -> str:
        """
        Returns a string representation of the Car object.

        :return: A string representation of the Car object.
        :rtype: str
        """
        formatted_price = "${:,.2f}".format(self.price)
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
            + self.state
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
