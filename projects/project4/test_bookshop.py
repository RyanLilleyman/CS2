from unittest import TestCase
from bookshop import BookShop


class Tests(TestCase):
    def __init__(self, orders):
        super().__init__()
        self.store = BookShop(orders)

    def test_one(self):
        result = self.store.total_price_per_book_order_number()
        check = [
            [1, ("5464", 49.96), ("8274", 233.82), ("9744", 404.55)],
            [2, ("5464", 99.91), ("9744", 404.55)],
            [3, ("5464", 99.91), ("88112", 274.89)],
            [4, ("8732", 93.93), ("7733", 208.89), ("88112", 199.75)],
        ]
        self.assertEqual(
            result,
            check,
            f"Expected to be {check}, but got {result}."
        )
        print("Test case no.1 passed!",end='\n\n')

    def test_two(self):
        result = self.store.filter_lowest()
        check = [(1, '5464'), (2, '5464'), (3, '5464'), (4, '873')]
        self.assertEqual(
            result,
            check,
        )
        print("Test case no.1 passed!",end='\n\n')

    def test_three(self):
        result = self.store.filter_l
        check = [(1, '5464'), (2, '5464'), (3, '5464'), (4, '873')]
        self.assertEqual(
            result,
            check,
        )
        print("Test case no.1 passed!",end='\n\n')

    def test_four(self):
        result = self.store.filter_lowest()
        check = [(1, '5464'), (2, '5464'), (3, '5464'), (4, '873')]
        self.assertEqual(
            result,
            check,
        )
        print("Test case no.1 passed!",end='\n\n')

    def test_five(self):
        result = self.store.filter_lowest()
        check = [(1, '5464'), (2, '5464'), (3, '5464'), (4, '873')]
        self.assertEqual(
            result,
            check,
        )
        print("Test case no.1 passed!",end='\n\n')

    def test_six(self):
        result = self.store.filter_lowest()
        check = [(1, '5464'), (2, '5464'), (3, '5464'), (4, '873')]
        self.assertEqual(
            result,
            check,
        )
        print("Test case no.1 passed!",end='\n\n')

    def test_seven(self):
        result = self.store.filter_lowest()
        check = [(1, '5464'), (2, '5464'), (3, '5464'), (4, '873')]
        self.assertEqual(
            result,
            check,
        )
        print("Test case no.1 passed!",end='\n\n')

    def test_eight(self):
        result = self.store.filter_lowest()
        check = [(1, '5464'), (2, '5464'), (3, '5464'), (4, '873')]
        self.assertEqual(
            result,
            check,
        )
        print("Test case no.1 passed!",end='\n\n')

    def test_ten(self):
        result = self.store.filter_lowest()
        check = [(1, '5464'), (2, '5464'), (3, '5464'), (4, '873')]
        self.assertEqual(
            result,
            check,
        )
        print("Test case no.1 passed!",end='\n\n')

    def test_nine(self):
        result = self.store.filter_lowest()
        check = [(1, '5464'), (2, '5464'), (3, '5464'), (4, '873')]
        self.assertEqual(
            result,
            check,
        )
        print("Test case no.1 passed!",end='\n\n')


