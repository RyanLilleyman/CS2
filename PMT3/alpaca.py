"""
Lab PMT
By Ryan Lilleyman
Date: November 28th, 2023
"""
from livestock import Livestock


class Alpaca(Livestock):
    """
    Alpaca Subclass
    """

    def __init__(self, age, weight):
        """
        Initializes an instance of the class with the given age and weight.

        Parameters:
            age (int): The age of the instance.
            weight (float): The weight of the instance.

        Returns:
            None
        """
        self.__weight = weight
        super().__init__(age)

    def get_weight(self):
        """
        Get the weight of the object.

        Returns:
            int: The weight of the object.
        """
        return self.__weight

    def get_price(self):
        """
        Calculate and return the price of an item based on its age and weight.

        Returns:
            Tuple[int, int]: A tuple containing two integers representing the price.
                - If the age of the item is less than or equal to 3, the price is 10,000.
                - If the age of the item is greater than 3 and the weight is less than or equal to 300, the price is 80,000.
                - If the age of the item is greater than 3 and the weight is greater than 300, the price is 100,000.
                - If the age or weight is invalid, the price is 0.
        """
        if self.get_age() <= 3:
            return 10000
        elif self.get_age() > 3 and self.get_weight() <= 300:
            return 80000
        elif self.get_age() > 3 and self.get_weight() > 300:
            return 100000
        else:
            return 0

    def get_animal_type(self):
        """
        Get the type of animal.
        """
        return "Alpaca"
