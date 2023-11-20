"""
Project: PMT
Author: Ryan Lilleyman
Date: 11/20/2023
Description: This is the class for the first class passenger.
"""

from ticket import Ticket


class First(Ticket):
    def __init__(self, name, date_of_birth, flight_number, miles):
        """
        Initializes a new instance of the class.

        Args:
            name (str): The name of the person.
            date_of_birth (str): The date of birth of the person.
            flight_number (str): The flight number.
            miles (int): The number of miles traveled.

        Returns:
            None
        """
        super().__init__(name, date_of_birth, flight_number, miles)
        self._set_discount_rate()
        self.set_ticket_cost(self.get_miles(), self.discount_rate)

    def _set_discount_rate(self, rate=0.85):
        """
        Set the discount rate for the object.

        Parameters:
            rate (float, optional): The discount rate to be set. Defaults to 0.85.

        Returns:
            None
        """
        self.discount_rate = rate

    def set_ticket_cost(self, miles, discount_rate):
        """
        Sets the ticket cost based on the number of miles and discount rate.

        Args:
            miles (int): The number of miles.
            discount_rate (float): The discount rate.

        Returns:
            None
        """
        self.ticket_cost = 10 * miles * discount_rate

    def get_type(self):
        """
        Get the type of the object.

        Returns:
            str: The type of the object.
        """
        return "First"
