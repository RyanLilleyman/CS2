"""
Project: PMT
Author: Ryan Lilleyman
Date: 11/20/2023
Description: This file contains the implementation of the First class.
"""
from ticket import Ticket


class Business(Ticket):
    def __init__(self, name, date_of_birth, flight_number, miles):
        """
        Initializes a new instance of the class.

        Args:
            name (str): The name of the passenger.
            date_of_birth (str): The date of birth of the passenger.
            flight_number (str): The flight number of the passenger.
            miles (int): The number of miles the passenger has traveled.

        Returns:
            None
        """
        super().__init__(name, date_of_birth, flight_number, miles)
        self._set_discount_rate()
        self.set_ticket_cost(self.get_miles(), self.discount_rate)

    def _set_discount_rate(self, rate=0.9):
        """
        Set the discount rate for the object.

        Args:
            rate (float, optional): The discount rate to be set. Defaults to 0.9.

        Returns:
            None
        """
        self.discount_rate = rate

    def set_ticket_cost(self, miles, discount_rate):
        """
        Sets the ticket cost based on the provided miles and discount rate.

        Parameters:
            miles (int): The number of miles traveled.
            discount_rate (float): The discount rate applied to the ticket cost.

        Returns:
            None
        """
        self.ticket_cost = 5 * miles * discount_rate

    def get_type(self):
        """
        Returns the type of the object.
        """
        return "Business"
