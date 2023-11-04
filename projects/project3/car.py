# Project No. 3
# Author: Ryan Lilleyman
# Description: Car super class.


class Car:
    """
    A class representing a car.

    Attributes:
        brand (str): The brand of the car.
        model (str): The model of the car.
        year (int): The year the car was manufactured.
        price (float): The price of the car.
        car_type (str): The type of the car.
    """

    def __init__(self, brand: str, model: str, year: int, price: float, car_type: str):
        self.__brand = brand
        self.__model = model
        self.__year = year
        self.__price = price
        self.__car_type = car_type

    @property
    def brand(self) -> str:
        """
        Returns the brand of the object.

        :return: A string representing the brand of the object.
        :rtype: str
        """
        return self.__brand

    @property
    def model(self) -> str:
        """
        Return the value of the 'model' attribute.

        :return: A string representing the value of the 'model' attribute.
        :rtype: str
        """
        return self.__model

    @property
    def year(self) -> int:
        """
        Get the value of the 'year' property.

        Returns:
            int: The value of the 'year' property.
        """
        return self.__year

    @property
    def price(self) -> float:
        """
        Return the price of the object.
        """
        return self.__price

    @property
    def car_type(self) -> str:
        """
        Get the car type.

        Returns:
            str: The car type.
        """
        return self.__car_type

    @brand.setter
    def brand(self, brand: str):
        """
        Set the brand of the object.

        Parameters:
            brand (str): The brand to be set.
        """
        self.__brand = brand

    @model.setter
    def model(self, model: str):
        """
        Set the value of the `model` attribute.

        :param model: The new value for the `model` attribute.
        :type model: str
        """
        self.__model = model

    @year.setter
    def year(self, year: int):
        """
        Set the value of the `year` attribute.

        Parameters:
            year (int): The new value for the `year` attribute.

        Returns:
            None
        """
        self.__year = year

    @price.setter
    def price(self, price: float):
        """
        Setter method for the 'price' attribute.

        Args:
            price (float): The new price value.

        Returns:
            None
        """
        self.__price = price

    @car_type.setter
    def car_type(self, car_type: str):
        """
        Setter method for the car_type attribute.

        Parameters:
            car_type (str): The new value for the car_type attribute.

        Returns:
            None
        """
        self.__car_type = car_type

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
        )

    def print_info(self):
        """
        Display the object by printing it.
        """
        print(self)
