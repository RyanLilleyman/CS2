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
        Initializes a new instance of the class.

        Args:
            orders (tuple, optional): A tuple of orders. Defaults to an empty tuple.

        Returns:
            None
        """
        self.orders = list(orders)
        self.mod = []

    def get_orders(self):
        """
        Get the orders.

        Returns:
            list: A list of orders.
        """
        return self.orders

    def set_orders(self, orders):
        """
        Set the orders for the current object.

        Parameters:
            orders (list): A list of orders.

        Returns:
            None
        """
        self.orders = orders

    def add_order(self, order):
        """
        Add an order to the list of orders.

        Parameters:
            order (object): The order to be added.

        Returns:
            None
        """
        self.orders.append(order)

    def step_one(self):
        """
        This function performs step one of the process. It iterates over the list of orders and modifies each order based on certain conditions. The modified orders are then appended to the `to_return` list. After the loop ends, the `to_return` list is assigned to the `mod` attribute of the class.

        Parameters:
            self: The instance of the class.

        Returns:
            list: The modified list of orders.
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

    def step_two(self):
        """
        Generates a list of tuples based on the `self.mod` attribute.

        :param self: The instance of the class.
        :return: A list of tuples containing the minimum value from each order in `self.mod`.

        The function iterates over each order in `self.mod` and finds the minimum value from each order using the `reduce` function.
        It then creates a new tuple with the order ID and the corresponding value with the minimum value.
        Finally, it appends the new tuple to the `fl` list and returns it.
        """
        fl = []
        for order in self.mod:
            minimum = reduce(
                lambda x, y: x if x < y else y, [item[1] for item in order[1:]]
            )
            bo = ""
            for tup in order[1:]:
                if tup[1] == minimum:
                    bo = tup[0]
            mo = (order[0], bo)
            fl.append(mo)
        return fl

    def step_three(self):
        """
        Generates a list of tuples based on the given `mod` list. Each tuple in the
        resulting list contains the first element of the corresponding order in the
        `mod` list and the element with the maximum value in the rest of the order.

        Returns:
            list: A list of tuples, where each tuple contains the first element of
            the order and the element with the maximum value in the rest of the order.
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

    def step_four(self):
        """
        This function iterates over a list of orders and performs some calculations on each order. It returns a new list with modified order data.

        Parameters:
            None

        Returns:
            list: A list of tuples where each tuple contains the order name and the total value calculated from the order data.
        """
        to_return = []
        for order in self.orders:
            mod = []

            on = order[0]
            mod.append(on)

            bol = order[1:]
            for book in bol:
                mbo = (book[0], (book[1] * book[2]))
                mod.append(mbo)

            to_return.append(mod)

        fl = []
        for order in to_return:
            tup = [item[1] for item in order[1:]]
            total = reduce(lambda x, y: x + y, tup)
            fl.append((order[0], float("{:,.2f}".format(total))))
        return fl

    def step_five(self):
        """
        Calculates the sum of the products of the second and third elements of each tuple in the orders list, grouped by the first element of each tuple.

        Returns a list containing the maximum value from the calculated sums and the maximum value from the sums' values.

        :param self: The current instance of the class.
        :return: A list containing the maximum value from the calculated sums and the maximum value from the sums' values.
        """
        di = {}

        for item in [
            tup for sublist in [order[1:] for order in self.orders] for tup in sublist
        ]:
            if item[0] in di.keys():
                di[item[0]] += item[1] * item[2]
            else:
                di[item[0]] = item[1] * item[2]

        return [
            str(reduce(lambda x, y: x if x > y else y, di)),
            reduce(lambda x, y: x if x > y else y, di.values()),
        ]

    def step_six(self):
        """
        Calculates the step six of the process.

        Returns:
            list: A list containing the highest value(s) in the dictionary.
        """
        di = {}
        for item in [
            tup for sublist in [order[1:] for order in self.orders] for tup in sublist
        ]:
            if item[0] in di.keys():
                di[item[0]] += item[1]
            else:
                di[item[0]] = item[1]

        x = list(
            filter(
                lambda x: di.get(x)
                == reduce(lambda x, y: x if x > y else y, di.values()),
                di,
            )
        )
        x.append(reduce(lambda x, y: x if x > y else y, di.values()))

        return x

    def step_seven(self):
        """
        Calculates the sum of values for each order in self.orders.

        Parameters:
            None

        Returns:
            A list of tuples containing the order ID and the sum of values for each order.
        """
        result = [
            (order[0], sum([item[1] for item in order[1:]])) for order in self.orders
        ]
        result = sorted(result, reverse=True, key=lambda x: x[1])
        return result

    def step_eight(self):
        """
        Calculates the total sum of all the items in the orders list.

        Returns:
            int: The total sum of all the items in the orders list.
        """
        result = [
            (order[0], reduce(lambda x, y: x + y, [item[1] for item in order[1:]]))
            for order in self.orders
        ]
        res = [item[1] for item in result]
        return reduce((lambda x, y: x + y), res)

    def step_nine(self):
        """
        Generates the result list by performing several operations on the self.orders list.

        Returns:
            list: The final list containing the desired elements.
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
        maximum = reduce(lambda x, y: x if x > y else y, n.values())
        ls = []
        for k in n:
            if n[k] == maximum:
                ls.append(k)

        minimum = reduce(lambda x, y: x if x < y else y, n.values())
        for k in n:
            if n[k] == minimum:
                ls.append(k)

        return ls

    def step_ten(self):
        """
        Calculate the length of each item in the orders list and return a list of the lengths.

        Returns:
            list: A list of integers representing the length of each item in the orders list.
        """
        return [len(item) for item in self.orders]

    def __str__(self):
        return str(self.orders)
