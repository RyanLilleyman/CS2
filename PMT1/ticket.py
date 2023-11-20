"""
Project: PMT
Author: Ryan Lilleyman
Date: 11/20/2023
Description: This is the class for the ticket.
"""


class Ticket:
    def __init__(self, name, date_of_birth, flight_number, miles):
        """
        Initializes the FlightPassenger object with the provided name, date of birth,
        flight number, and miles.

        Parameters:
            name (str): The name of the passenger.
            date_of_birth (str): The date of birth of the passenger.
            flight_number (str): The flight number of the passenger.
            miles (int): The number of miles the passenger has travelled.

        Returns:
            None
        """
        self.__name = name
        self.__date_of_birth = date_of_birth
        self.__flight_number = flight_number
        self.__miles = miles
        self.__type = type(self)
        self.discount_rate = 0
        self.ticket_cost = 0

    # getters
    def get_name(self):
        """
        Returns the name of the object.

        :return: (str) The name of the object.
        """
        return self.__name

    def get_dob(self):
        """
        Get the date of birth of the object.

        Returns:
            The date of birth of the object.
        """
        return self.__date_of_birth

    def get_flight_number(self):
        """
        Get the flight number.

        Returns:
            str: The flight number.
        """
        return self.__flight_number

    def get_miles(self):
        """
        Get the value of the `miles` attribute.

        Returns:
            The value of the `miles` attribute.
        """
        return self.__miles

    def get_ticket_cost(self):
        """
        Get the ticket cost.

        Returns:
            float: The cost of the ticket.
        """
        return self.ticket_cost

    def get_type(self):
        """
        Get the type of the object.

        :return: The type of the object.
        """
        return self.__type

    def get_discount_rate(self):
        """
        Get the discount rate.

        Returns:
            The discount rate.
        """
        return self.discount_rate

    # setters
    def set_name(self, name):
        """
        Sets the name of the object.

        Parameters:
            name (str): The new name for the object.

        Returns:
            None
        """
        self.__name = name

    def set_dob(self, dob):
        """
        Set the date of birth for the object instance.

        Args:
            dob (datetime): The date of birth to set.

        Returns:
            None
        """
        self.__date_of_birth = dob

    def set_flight_number(self, fn):
        """
        Set the flight number for the object.

        Parameters:
            fn (str): The flight number to be set.

        Returns:
            None
        """
        self.__flight_number = fn

    def set_miles(self, miles):
        """
        Set the value of the miles attribute.

        Parameters:
            miles (any): The new value for the miles attribute.

        Returns:
            None
        """
        self.__miles = miles

    def set_ticket_cost(self, miles, discount_rate):
        """
        Set the ticket cost based on the number of miles and the discount rate.

        Parameters:
            miles (int): The number of miles traveled.
            discount_rate (float): The discount rate applied to the ticket cost.

        Returns:
            None
        """
        self.ticket_cost = miles * discount_rate

    def _set_discount_rate(self, rate):
        """
        Set the discount rate for the object.

        Parameters:
            rate (float): The new discount rate to be set.

        Returns:
            None
        """
        self.discount_rate = rate
