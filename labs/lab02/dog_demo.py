import dog


def main():
    newDog = dog.Dog("Fido", 3, "Boston Terrier")
    newDog.eat("Dog Food")
    newDog.sleep(3)
    newDog.bark()
    print(newDog)


if __name__ == "__main__":
    main()
