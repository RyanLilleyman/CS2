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
        Executes test case no.1 by calling the `step_one` method of the `store` object.
        The expected result is a list of lists, where each inner list contains an integer
        followed by a tuple of strings and floats. The function compares the result with
        a predefined check list and asserts that they are equal. If the assertion passes,
        a success message is printed to the console.

        Parameters:
        - self: The instance of the test class.

        Returns:
        - None
        """
        result = self.store.step_one()
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

    def test_two(self):
        """
        Executes the second test case by calling the `step_two` method of the `store` object and comparing the result with the expected `check` value.

        Parameters:
            self (TestClass): The instance of the TestClass.

        Returns:
            None
        """
        result = self.store.step_two()
        check = [(1, "5464"), (2, "5464"), (3, "5464"), (4, "8732")]
        format_string = f"Expected:\n\n {check}, got\n\n {result}"

        self.assertEqual(result, check, format_string)
        print()
        print("Test case no.2 passed!", end="\n\n")

    def test_three(self):
        """
        Executes the third test case for the `test_three` method.

        This method calls the `step_three` method of the `store` object and assigns the result to the `result` variable.

        It checks if the `result` matches the expected value stored in the `check` list.

        If the `result` does not match the expected value, an assertion error is raised with a formatted error message.

        After the test case is executed, a success message is printed.

        Parameters:
            self (TestClass): The object instance.

        Returns:
            None
        """
        result = self.store.step_three()
        check = [(1, "9744"), (2, "9744"), (3, "88112"), (4, "7733")]
        format_string = f"Expected:\n\n {check}, got\n\n {result}"

        self.assertEqual(
            result,
            check,
            format_string,
        )
        print()
        print("Test case no.3 passed!", end="\n\n")

    def test_four(self):
        """
        Executes step four of the test process.

        :return: None
        """
        result = self.store.step_four()
        check = [(1, 678.33), (2, 494.46), (3, 364.8), (4, 492.57)]
        format_string = f"Expected:\n\n {check}, got\n\n {result}"

        self.assertEqual(result, check, format_string)
        print()
        print("Test case no.4 passed!", end="\n\n")

    def test_five(self):
        """
        Executes test case five.

        This function calls the `step_five` method of the `store` object and assigns the returned value to the `result` variable.
        It then compares the value of `result` with the expected value stored in the `check` list.
        If the values are not equal, it raises an `AssertionError` with a formatted string that displays the expected and actual values.
        Finally, it prints a success message if the test case passes.

        Parameters:
        - self: The current instance of the class.

        Returns:
        - None
        """
        result = self.store.step_five()
        check = ["9744", 809.1]
        format_string = f"Expected:\n\n {check}, got\n\n {result}"

        self.assertEqual(result, check, format_string)
        print()
        print("Test case no.5 passed!", end="\n\n")

    def test_six(self):
        """
        Executes test case no. 6 for the function `step_six` of the `store` object.

        Parameters:
            None

        Returns:
            None
        """
        result = self.store.step_six()
        check = ["5464", 22]
        format_string = f"Expected:\n\n {check}, got\n\n {result}"

        self.assertEqual(result, check, format_string)
        print()
        print("Test case no.6 passed!", end="\n\n")

    def test_seven(self):
        """
        Test the step_seven method of the store.

        :return: None
        """
        result = self.store.step_seven()
        check = [(1, 31), (4, 23), (3, 20), (2, 18)]
        format_string = f"Expected:\n\n {check}, got\n\n {result}"

        self.assertEqual(result, check, format_string)
        print()
        print("Test case no.7 passed!", end="\n\n")

    def test_eight(self):
        """
        This function is a test case for step eight of the process. It calls the `step_eight` method of the `store` object and assigns the result to the `result` variable. It then checks if the `result` is equal to the expected value `92`. If the result and expected value are not equal, it formats a string to display the expected and actual values. Finally, it asserts that the `result` is equal to the expected value and prints a success message if the test case passes.
        """
        result = self.store.step_eight()
        check = 92
        format_string = f"Expected:\n\n {check}, got\n\n {result}"

        self.assertEqual(
            result,
            check,
            format_string,
        )
        print()
        print("Test case no.8 passed!", end="\n\n")

    def test_nine(self):
        """
        Executes test case number nine.
        """
        result = self.store.step_nine()
        check = ["5464", "8732"]
        format_string = f"Expected:\n\n {check}, got\n\n {result}"

        self.assertEqual(result, check, format_string)
        print()
        print("Test case no.9 passed!", end="\n\n")

    def test_ten(self):
        """
        Test method to verify the behavior of the 'test_ten' function.

        This method performs the following steps:
        1. Calls the 'step_ten' method of the 'store' object.
        2. Assigns the returned value to the 'result' variable.
        3. Initializes the 'check' list with the expected values.
        4. Constructs a format string to display the expected and actual results.
        5. Asserts that the 'result' is equal to the 'check' list, using the constructed format string as the error message.
        6. Prints a blank line.
        7. Prints a success message indicating that test case no.10 has passed.

        This method does not have any parameters.

        This method does not return any values.
        """
        result = self.store.step_ten()
        check = [4, 3, 3, 4]
        format_string = f"Expected:\n\n {check}, got\n\n {result}"

        self.assertEqual(
            result,
            check,
            format_string,
        )
        print()
        print("Test case no.10 passed!", end="\n\n")
