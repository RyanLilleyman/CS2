"""
Project No. 4
Authors: Ryan Lilleyman, Christian Blanchard
Description: Test Class
"""

from unittest import TestCase
from bookshop import BookShop


class Tests(TestCase):
    """
    This class contains unit tests for the BookShop class.
    """

    def __init__(self, orders):
        """
        Initializes a new instance of the class.

        Parameters:
            orders (list): A list of orders.

        Returns:
            None
        """
        super().__init__()
        self.store = BookShop(orders)

    def test_one(self):
        """
        Test the functionality of the `total_price_per_book_order_number` method.

        This method retrieves the total price of each book for each order number.

        Parameters:
        - None

        Returns:
        - result (list): A list of lists containing the order number and the total price of each book for that order number.
          Each inner list contains:
          - order_number (int): The order number.
          - book_price (tuple): A tuple containing the book ID and its total price.
            - book_id (str): The ID of the book.
            - total_price (float): The total price of the book.

        Example:
        [
            [1, ("5464", 49.96), ("8274", 233.82), ("9744", 404.55)],
            [2, ("5464", 99.91), ("9744", 404.55)],
            [3, ("5464", 99.91), ("88112", 274.89)],
            [4, ("8732", 93.93), ("7733", 208.89), ("88112", 199.75)],
        ]
        """
        result = self.store.total_price_per_book_order_number()
        check = [
            [1, ("5464", 49.96), ("8274", 233.82), ("9744", 404.55)],
            [2, ("5464", 99.91), ("9744", 404.55)],
            [3, ("5464", 99.91), ("88112", 274.89)],
            [4, ("8732", 93.93), ("7733", 208.89), ("88112", 199.75)],
        ]
        format_string = f"Expected:\n\n {check}, got\n\n {result}"
        self.assertEqual(result, check, format_string)
        print()
        print("Test case no.1 passed!", end="\n\n")
        print(format_string, end="\n")

    def test_two(self):
        """
        This function is used to test the 'filter_lowest' method of the 'store' object. It calls the 'filter_lowest' method and compares the returned value with the expected value. The expected value is a list of tuples containing integers and strings. This function asserts that the returned value is equal to the expected value. Finally, it prints a success message if the test case passes.

        Parameters:
            self (object): The current instance of the class.

        Returns:
            None
        """
        result = self.store.filter_lowest()
        check = [(1, "5464"), (2, "5464"), (3, "5464"), (4, "8732")]
        format_string = f"Expected:\n\n {check}, got\n\n {result}"

        self.assertEqual(result, check, format_string)
        print()
        print("Test case no.2 passed!", end="\n\n")
        print(format_string, end="\n")

    def test_three(self):
        """
        Test the 'filter_maximum' method of the 'store' object.

        This method calls the 'filter_maximum' method of the 'store' object and stores the result in the 'result' variable.
        Then it checks if the 'result' variable is equal to the 'check' variable.
        The 'check' variable is a list of tuples, where each tuple represents an expected value for the corresponding index of the 'result' variable.
        If the assertion passes, it prints a success message.

        Parameters:
            self (object): The current instance of the test class.

        Returns:
            None
        """
        result = self.store.filter_maximum()
        check = [(1, "9744"), (2, "9744"), (3, "88112"), (4, "7733")]
        format_string = f"Expected:\n\n {check}, got\n\n {result}"

        self.assertEqual(
            result,
            check,
            format_string,
        )
        print()
        print("Test case no.3 passed!", end="\n\n")
        print(format_string, end="\n")

    def test_four(self):
        """
        Test the `sum_tuple` method of the `store` object and assert if the result matches the expected value.
        """
        result = self.store.sum_tuple()
        check = [(1, "688.33"), (2, "504.46"), (3, "374.80"), (4, "502.57")]
        format_string = f"Expected:\n\n {check}, got\n\n {result}"

        self.assertEqual(result, check, format_string)
        print()
        print("Test case no.4 passed!", end="\n\n")
        print(format_string, end="\n")

    def test_five(self):
        """
        Test the functionality of the `max_amount` method in the `store` object.
        """
        result = self.store.max_amount()
        check = [1, 688.33]
        format_string = f"Expected:\n\n {check}, got\n\n {result}"

        self.assertEqual(result, check, format_string)
        print()
        print("Test case no.5 passed!", end="\n\n")
        print(format_string, end="\n")

    def test_six(self):
        """
        Test case for the test_six method.

        This test case checks if the max_order_and_book method of the store object returns the correct result. It verifies that the result is equal to the tuple (1, 31).

        Returns:
            None
        """
        result = self.store.max_order_and_book()
        check = [1, 31]
        format_string = f"Expected:\n\n {check}, got\n\n {result}"

        self.assertEqual(result, check, format_string)
        print()
        print("Test case no.6 passed!", end="\n\n")
        print(format_string, end="\n")

    def test_seven(self):
        """
        Test the `max_books_decending_list` method of the `store` object.

        This test case verifies that the `max_books_decending_list` method of the `store` object returns the expected result.

        Parameters:
        self -- the current instance of the test case

        Returns:
        None
        """
        result = self.store.max_books_decending_list()
        check = [(4, 23), (3, 20), (2, 18), (1, 31)]
        format_string = f"Expected:\n\n {check}, got\n\n {result}"

        self.assertEqual(
            result,
            check,
        )
        print()
        print("Test case no.7 passed!", end="\n\n")
        print(format_string, end="\n")

    def test_eight(self):
        """
        Test case to check the functionality of the `total_quantity_of_all_books` method.

        This test case verifies that the `total_quantity_of_all_books` method returns the correct total quantity of all books in the store.

        Parameters:
            self (object): The instance of the test class.

        Returns:
            None
        """
        result = self.store.total_quantity_of_all_books()
        check = 92
        format_string = f"Expected:\n\n {check}, got\n\n {result}"

        self.assertEqual(
            result,
            check,
            format_string,
        )
        print()
        print("Test case no.8 passed!", end="\n\n")
        print(format_string, end="\n")

    def test_nine(self):
        """
        Test case for the `test_nine` method.

        This test case verifies that the `most_ordered` method of the `store` object returns the correct result.

        It performs the following steps:
        - Calls the `most_ordered` method of the `store` object.
        - Compares the result with the expected value.
        - Prints a success message if the test case passes.

        Returns:
        None
        """
        result = self.store.most_ordered()
        check = ["5464", "8732"]
        format_string = f"Expected:\n\n {check}, got\n\n {result}"

        self.assertEqual(result, check, format_string)
        print()
        print("Test case no.9 passed!", end="\n\n")
        print(format_string, end="\n")

    def test_ten(self):
        """
        Executes test case number 10 for the `test_ten` method.

        This method tests the functionality of the `test_ten` method by calling the `self.store.sub_order_length()` method and comparing the result to the expected value.

        Parameters:
            None

        Returns:
            None
        """
        result = self.store.sub_order_length()
        check = [3, 2, 2, 3]
        format_string = f"Expected:\n\n {check}, got\n\n {result}"

        self.assertEqual(
            result,
            check,
            format_string,
        )
        print()
        print("Test case no.10 passed!", end="\n\n")
        print(format_string, end="\n")
