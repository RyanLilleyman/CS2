import random


def main():
    with open("capitals.txt", "r") as f:
        lines = f.readlines()
        capitals = {}
        for line in lines:
            k, v = line.split(",")
            capitals[k] = v
    playAgain = True
    print("We are going to play a little capital guessing game.")
    while playAgain:
        secretState = random.sample(list(capitals.items()), 1)
        secretState = list(secretState[0])
        print(f"Enter in your guess for the capital of {secretState[0]}?")
        guess = str(input())

        if guess == secretState[1].rstrip("\n"):
            print("Nice")
        else:
            print("Oops! Too bad. You made a blunder.")

        while True:
            print("Again?")
            answer = str(input())
            answer.lower()
            answer = answer[0]
            if answer == "y":
                break
            elif answer == "n":
                playAgain = False
                break
            else:
                print("Invalid! Try Again")
                continue


if __name__ == "__main__":
    main()
