"""
Project No. 4
Authors: Ryan Lilleyman, Christian Blanchard
Description: Book Class
"""

from functools import reduce
from collections import defaultdict


class BookShop:
    """
    Represents a book shop.

    This class manages orders and provides methods for handling book-related operations.
    """

    def __init__(self, orders=()):
        """
        Initializes an instance of the class.

        Parameters:
            orders (list, optional): A list of orders. Defaults to an empty list.
        """
        self.orders = list(orders)
        self.mod = []
        self.mo = []

    def get_orders(self):
        """
        Get the orders.

        Returns:
            The orders.
        """
        return self.orders

    def set_orders(self, orders):
        """
        Set the orders for the object.

        Parameters:
            orders (list): A list of orders to be set.

        Returns:
            None
        """
        self.orders = orders

    def add_order(self, order):
        """
        Add an order to the list of orders.

        Args:
            order: The order to be added.

        Returns:
            None.
        """
        self.orders.append(order)

    def total_price_per_book_order_number(self):
        """
        Calculates the total price per book order number.

        Returns:
            list: A list of modified order numbers and their corresponding total prices.
        """
        to_return = []
        for order in self.orders:
            mod = []

            on = order[0]
            mod.append(on)

            bol = order[1:]
            for book in bol:
                if book[1] * book[2] < 100:
                    mbo = (book[0], (book[1] * book[2]) + 10)
                    mod.append(mbo)
                else:
                    mbo = (book[0], (book[1] * book[2]))
                    mod.append(mbo)

            to_return.append(mod)

        self.mod = to_return
        return to_return

    def filter_lowest(self):
        """
        Generates a new list of tuples containing the lowest value from each order in the `mod` list of the class.

        Returns:
            list: A list of tuples containing the lowest value from each order. Each tuple consists of the order's id and the item with the lowest value.
        """
        fl = []
        for order in self.mod:
            tup = [item[1] for item in order[1:]]
            minimum = list(filter(lambda x: x == min(tup), tup))
            minimum = minimum[0]
            bo = ""
            for tup in order[1:]:
                if tup[1] == minimum:
                    bo = tup[0]
            mo = (order[0], bo)
            fl.append(mo)
        return fl

    def filter_maximum(self):
        """
        Filters the maximum values from each order in the `self.mod` list and returns a list of tuples containing the order number and the item with the maximum value.

        Returns:
            list: A list of tuples, each containing the order number and the item with the maximum value.
        """
        fl = []
        for order in self.mod:
            tup = [item[1] for item in order[1:]]
            maximum = list(filter(lambda x: x == max(tup), tup))
            maximum = maximum[0]

            bo = ""
            for tup in order[1:]:
                if tup[1] == maximum:
                    bo = tup[0]

            mo = (order[0], bo)

            fl.append(mo)
        return fl

    def sum_tuple(self):
        """
        Calculate the sum of all tuples in the `mod` list.

        Returns:
            list: A list of tuples containing the order ID and the total sum of each tuple as a formatted string.
        """
        fl = []
        for order in self.mod:
            tup = [item[1] for item in order[1:]]
            total = reduce(lambda x, y: x + y, tup)
            fl.append((order[0], "{:,.2f}".format(total)))
        return fl

    def max_amount(self):
        """
        Find the maximum amount in the sum_tuple list.

        Parameters:
        - None

        Returns:
        - A list containing the item with the maximum amount from the sum_tuple list. The list contains two elements: the item's name and the item's amount, represented as a float.
        """
        to_max = max([item[1] for item in self.sum_tuple()])
        for tup in self.sum_tuple():
            if tup[1] == to_max:
                return [tup[0], float(tup[1])]

    def max_order_and_book(self):
        """
        Calculate the maximum order and book.

        This function iterates over the list of orders and calculates the total sum of the order items. It then finds the maximum sum and filters the orders with the maximum sum. Finally, it returns the first order with the maximum sum.

        Parameters:
        - self: The instance of the current class.

        Returns:
        - result: A tuple representing the maximum order and its sum.
        """
        result = [
            (order[0], sum([item[1] for item in order[1:]])) for order in self.orders
        ]
        res = max([item[1] for item in result])
        something = list(filter(lambda x: x[1] == res, result))
        result = something[0]
        return result

    def max_books_decending_list(self):
        """
        Generates a list of tuples containing the total number of books and the sum of their quantities for each order in descending order.

        Returns:
            list: A list of tuples in descending order. Each tuple contains the order ID and the total quantity of books.
        """
        result = [
            (order[0], sum([item[1] for item in order[1:]])) for order in self.orders
        ]
        result = sorted(result, reverse=True)
        return result

    def total_quantity_of_all_books(self):
        """
        Calculates the total quantity of all books in the orders.

        Returns:
            int: The total quantity of all books.
        """
        result = [
            (order[0], sum([item[1] for item in order[1:]])) for order in self.orders
        ]
        res = [item[1] for item in result]
        return reduce((lambda x, y: x + y), res)

    def most_ordered(self):
        """
        Returns a list of items that are most ordered and least ordered.

        This function iterates over the list of orders and extracts the items from each order.
        For each item, it keeps track of the total quantity by updating the quantity in a dictionary.
        After iterating over all the orders, it finds the maximum and minimum quantities.
        It then adds the items with the maximum quantity to a list and the items with the minimum quantity to the same list.
        Finally, it returns the list of items.

        Returns:
            list: A list of items that are most ordered and least ordered.
        """
        result = [item for item in [order[1:] for order in self.orders]]
        n = defaultdict(str)
        for res in result:
            for item in res:
                key = item[0]
                value = item[1]

                if key in n:
                    n[key] += value
                else:
                    n[key] = value
        maximum = max(n.values())
        ls = []
        for k in n:
            if n[k] == maximum:
                ls.append(k)

        minimum = min(n.values())
        for k in n:
            if n[k] == minimum:
                ls.append(k)

        return ls

    def sub_order_length(self):
        """
        Calculates the length of each sublist in the `orders` attribute.

        Parameters:
            self (ClassName): An instance of the ClassName class.

        Returns:
            list: A list containing the lengths of each sublist in `orders`.
        """
        sublist = [item for item in [order[1:] for order in self.orders]]
        lengths = [len(item) for item in sublist]
        return lengths

    def __str__(self):
        """
        Returns a string representation of the 'orders' attribute.

        :return: A string representation of the 'orders' attribute.
        :rtype: str
        """
        return str(self.orders)
