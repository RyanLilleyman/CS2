"""
Lab PMT
By Ryan Lilleyman
Date: November 28th, 2023
"""


class FarmApp:
    """
    Farm App class
    """

    def __init__(self):
        """
        Initializes a new instance of the class.

        Parameters:
            None

        Returns:
            None
        """
        self.__animals = []

    def get_livestock(self):
        """
        Returns the list of livestock animals.

        :return: The list of livestock animals.
        """
        return self.__animals

    def add_livestock(self, livestock):
        """
        Add a new livestock to the list of animals.

        Parameters:
            livestock (object): The livestock object to be added.

        Returns:
            None
        """
        self.__animals.append(livestock)

    def get_totoal_price(self):
        """
        Calculate and return the total price of all animals in the __animals list.

        Returns:
            float: The total price of all animals.
        """
        return sum([animal.get_price() for animal in self.__animals])
