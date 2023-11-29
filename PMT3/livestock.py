"""
Lab PMT
By Ryan Lilleyman
Date: November 28th, 2023
"""


class Livestock:
    """
    Livestock class
    """

    def __init__(self, age):
        """
        Initializes an instance of the class with the specified age.

        Parameters:
            age (int): The age of the instance.

        Returns:
            None
        """
        self.__age = age

    def get_age(self):
        """
        Get the age of the object.

        Returns:
            int: The age of the object.
        """
        return self.__age

    def get_animal_type(self):
        pass

    def get_price(self):
        pass
