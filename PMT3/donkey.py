"""
Lab PMT
By Ryan Lilleyman
Date: November 28th, 2023
"""
from livestock import Livestock


class Donkey(Livestock):
    """
    Donkey Subclass
    """

    def __init__(self, age, breed):
        """
        Initializes a new instance of the class.

        :param age: The age of the instance.
        :type age: int
        :param breed: The breed of the instance.
        :type breed: str
        """
        super().__init__(age)
        self.__breed = breed

    def get_breed(self):
        """
        Get the breed of the object.

        :return: The breed of the object.
        """
        return self.__breed

    def get_price(self):
        """
        Calculate and return the price of a donkey based on its age and breed.

        Parameters:
            None.

        Returns:
            Tuple[int, int]: A tuple containing the price of the donkey as the first element
            and the price in cents as the second element. If the donkey's age is less than or
            equal to 3, the price is 20,000 cents. If the donkey's age is greater than 3 and
            its breed is "Miniature", the price is 100,000 cents. If the donkey's age is
            greater than 3 and its breed is "American Mammoth Jack", the price is 180,000
            cents. If the donkey's age is greater than 3 and its breed is "Burro", the price
            is 120,000 cents. If the donkey's age is greater than 3 and its breed is not
            "Miniature", "American Mammoth Jack", or "Burro", the price is 0 cents.

        """
        if self.get_age() <= 3:
            return 20000
        elif self.get_age() > 3 and self.get_breed() == "Miniature":
            return 100000
        elif self.get_age() > 3 and self.get_breed() == "American Mammoth Jack":
            return 180000
        elif self.get_age() > 3 and self.get_breed() == "Burro":
            return 120000
        else:
            return 0

    def get_animal_type(self):
        """
        Get the type of animal.
        """
        return "Donkey"
