"""
Lab PMT
By Ryan Lilleyman
Date: November 28th, 2023
"""
from livestock import Livestock


class Camel(Livestock):
    """
    Camel Subclass
    """

    def __init__(self, age, numberOfHumps):
        """
        Initializes a new instance of the class.

        Parameters:
            age (int): The age of the instance.
            numberOfHumps (int): The number of humps of the instance.

        Returns:
            None
        """
        self.__numberOfHumps = numberOfHumps
        super().__init__(age)

    def get_numberOfHumps(self):
        """
        Get the number of humps.

        Returns:
            int: The number of humps.
        """
        return self.__numberOfHumps

    def get_price(self):
        """
        Returns the price of an item based on its age and number of humps.

        Parameters:
            None

        Returns:
            tuple: A tuple containing two values - the price of the item in thousands and the price of the item in hundreds.
                  The price is determined based on the age and the number of humps of the item.
                  If the age of the item is less than or equal to 3, the price is 50,000.
                  If the age of the item is greater than 3 and the number of humps is 2, the price is 150,000.
                  If the age of the item is greater than 3 and the number of humps is 3, the price is 200,000.
                  If the age of the item is greater than 3 and the number of humps is neither 2 nor 3, the price is 0.
        """
        if self.get_age() <= 3:
            return 50000
        elif self.get_age() > 3 and self.get_numberOfHumps() == 2:
            return 150000
        elif self.get_age() > 3 and self.get_numberOfHumps() == 3:
            return 200000
        else:
            return 0

    def get_animal_type(self):
        """
        Get the type of animal.
        """
        return "Camel"
