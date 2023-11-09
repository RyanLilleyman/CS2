"""
Project No. 4
Authors: Ryan Lilleyman, Christian Blanchard
Description: Main Python File
"""
from bookshop import BookShop
from test_bookshop import Tests


def main():
    """
    Generate the function comment for the following function:

    Args:
        None

    Returns:
        None
    """
    orders = [
        [1, ("5464", 4, 9.99), ("8274", 18, 12.99), ("9744", 9, 44.95)],
        [2, ("5464", 9, 9.99), ("9744", 9, 44.95)],
        [3, ("5464", 9, 9.99), ("88112", 11, 24.99)],
        [4, ("8732", 7, 11.99), ("7733", 11, 18.99), ("88112", 5, 39.95)],
    ]

    store = BookShop(orders)
    print()
    print(store.total_price_per_book_order_number(), end="\n\n")
    print(store.filter_lowest(), end="\n\n")
    print(store.filter_maximum(), end="\n\n")
    print(store.sum_tuple(), end="\n\n")
    print(store.max_amount(), end="\n\n")
    print(store.max_order_and_book(), end="\n\n")
    print(store.max_books_decending_list(), end="\n\n")
    print(store.total_quantity_of_all_books(), end="\n\n")
    print(store.most_ordered(), end="\n\n")
    print(store.sub_order_length(), end="\n\n")

    print("Tests", end="\n\n")
    tst = Tests(orders)
    print(tst.test_one())
    print(tst.test_two())
    print(tst.test_three())
    print(tst.test_four())
    print(tst.test_five())
    print(tst.test_six())
    print(tst.test_seven())
    print(tst.test_eight())
    print(tst.test_nine())
    print(tst.test_ten())


if __name__ == "__main__":
    main()
