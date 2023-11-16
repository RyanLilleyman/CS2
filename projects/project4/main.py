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
    print(store.step_one(), end="\n\n")
    print(store.step_two(), end="\n\n")
    print(store.step_three(), end="\n\n")
    print(store.step_four(), end="\n\n")
    print(store.step_five(), end="\n\n")
    print(store.step_six(), end="\n\n")
    print(store.step_seven(), end="\n\n")
    print(store.step_eight(), end="\n\n")
    print(store.step_nine(), end="\n\n")
    print(store.step_ten(), end="\n\n")

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
