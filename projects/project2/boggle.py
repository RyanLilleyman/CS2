# Project No: 2
# Author: Ryan Lilleyman
# Description: This is the main class that governs the boggle game logic.


import random
import string


class BoggleBoard:
    # Attribute Definition
    def __init__(self) -> None:
        self.__board = [
            [" ", " ", " ", " "],
            [" ", " ", " ", " "],
            [" ", " ", " ", " "],
            [" ", " ", " ", " "],
        ]
        self.__seed = None
        self.__current_guess = ""

    # Display the Board
    def __str__(self):
        return f""" 
        +---+ +---+ +---+ +---+
        | {self.__board[0][0]} | | {self.__board[0][1]} | | {self.__board[0][2]} | | {self.__board[0][3]} |
        +---+ +---+ +---+ +---+
        +---+ +---+ +---+ +---+
        | {self.__board[1][0]} | | {self.__board[1][1]} | | {self.__board[1][2]} | | {self.__board[1][3]} |
        +---+ +---+ +---+ +---+
        +---+ +---+ +---+ +---+
        | {self.__board[2][0]} | | {self.__board[2][1]} | | {self.__board[2][2]} | | {self.__board[2][3]} |
        +---+ +---+ +---+ +---+
        +---+ +---+ +---+ +---+
        | {self.__board[3][0]} | | {self.__board[3][1]} | | {self.__board[3][2]} | | {self.__board[3][3]} |
        +---+ +---+ +---+ +---+
        """

    # Some Getters
    def get_board(self):
        return self.__board

    def get_seed(self):
        return self.__seed

    def get_current_guess(self):
        return self.__current_guess

    # Fill Board with current seed.
    def fill_board(self):
        random.seed(self.__seed)
        for i, row in enumerate(self.__board):
            for j, value in enumerate(row):
                value = random.choice(string.ascii_uppercase)
                self.__board[i][j] = value
        print(self)

    # Set the seed to a specific value
    def set_seed(self):
        num = int(input("Enter in the seed value: "))
        while (num < 0) or (num > 9999):
            print("Number must be within 0 and 9999.")
            num = int(input("Enter in the seed value: "))
        self.__seed = num

    # Randomize the Current Seed
    def set_seed_random(self):
        self.__seed = None

    def guess(self):
        s = str(input("Enter a word (preferably Uppercase): "))
        self.__current_guess = s
        print(self.__current_guess)
        if self.check_palindrome(self.clean_guess()):
            self.is_a_pal()
        else:
            self.not_a_pal()

    def clean_guess(self):
        return self.__current_guess.upper()

    def check_neighbors(self, i, j, c):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for r, c in directions:
            newI, newJ = i + r, j + c
            if 0 < newI < 4 and 0 < newJ < 4:
                if self.__board[newI][newJ] == c:
                    return True
        return False

    def check_guess_validity(self, s, kdx=0):
        if kdx == len(s):
            return True
        print(s[kdx])
        curr = s[kdx]
        print(curr)
        for i in range(len(self.get_board())):
            for j in range(4):
                if self.__board[i][j] == curr:
                    print(True)
                    if self.check_neighbors(i, j, curr):
                        if self.check_guess_validity(s, kdx + 1):
                            return True
        return False

    def not_a_pal(self):
        print(f"The word {self.__current_guess} is not a palindrome.")

    def is_a_pal(self):
        print(f"The word {self.__current_guess} is a palindrome.")

    # Recursive function to find if a palindrome.
    def check_palindrome(self, s):
        i = 0
        j = len(s) - 1
        if i > j:
            return True
        if s[i] != s[j]:
            return False
        else:
            s = s[i + 1 : j]
            return self.check_palindrome(s)

    # Greet player in game loop
    def greetings(self):
        return """
        Welcome to a simple 4 x 4 boggle game.
 
            1. Enter in a seed. If you want a random seed,
            just hit the enter button.
            2. Enter an UPPERcase word to guess.
            3. Continue the game loop or stop with yes or no.
        """

    # Test conditions
    def test_set_seed(self):
        self.greetings()
        self.set_seed()
        self.fill_board()

    def test_case_one(self):
        self.greetings()
        self.set_seed()
        self.fill_board()
        self.guess()
