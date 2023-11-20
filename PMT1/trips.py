"""
Project: PMT
Author: Ryan Lilleyman
Date: 11/20/2023
Description: This file contains the implementation of the Trips class.
"""


class Trips:
    def __init__(self):
        """
        Initializes the class by setting the total travel cost to 0 and creating an empty list for tickets.

        Parameters:
            None

        Returns:
            None
        """
        self.__total_travel_cost = 0
        self.__tickets = []

    def get_tickets(self):
        """
        Returns the list of tickets associated with the object.

        :return: list of tickets
        """
        return self.__tickets

    def add_ticket(self, ticket):
        """
        Adds a ticket to the list of tickets.

        Parameters:
            ticket (Ticket): The ticket to be added.

        Returns:
            None
        """
        self.__tickets.append(ticket)

    def get_total_travel_cost(self):
        """
        Calculate the total travel cost.

        This function iterates through each ticket in the list of tickets (__tickets) and
        adds the cost of each ticket to the total cost. The total cost is then returned.

        Parameters:
        - None

        Returns:
        - total (float): The total cost of travel.

        """
        total = 0
        for ticket in self.__tickets:
            total += ticket.get_ticket_cost()
        return total
