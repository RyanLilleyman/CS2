"""
Project: PMT
Author: Ryan Lilleyman
Date: 11/23/2023
Description: This file contains the implementation of the Economy class.
"""
from ticket import Ticket


class Economy(Ticket):
    def __init__(self, name, date_of_birth, flight_number, miles):
        """
        Initializes a new instance of the class with the specified name, date of birth, flight number, and miles.

        Parameters:
            name (str): The name of the passenger.
            date_of_birth (str): The date of birth of the passenger.
            flight_number (str): The flight number of the passenger's flight.
            miles (int): The number of miles the passenger has accumulated.

        Returns:
            None
        """
        super().__init__(name, date_of_birth, flight_number, miles)
        self._set_discount_rate()
        self.set_ticket_cost(self.get_miles(), self.discount_rate)

    def _set_discount_rate(self, rate=0.95):
        """
        Set the discount rate for the object.

        Parameters:
            rate (float): The discount rate to be set. Default is 0.95.

        Returns:
            None
        """
        self.discount_rate = rate

    def set_ticket_cost(self, miles, discount_rate):
        """
        Set the ticket cost based on the provided miles and discount rate.

        Parameters:
            miles (float): The number of miles traveled.
            discount_rate (float): The discount rate applied to the ticket cost.

        Returns:
            None
        """
        self.ticket_cost = miles * discount_rate

    def get_type(self):
        """
        Returns the type of the object.
        """
        return "Economy"
