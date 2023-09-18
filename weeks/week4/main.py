import pet


def main():
    name = input("Please enter pet's name:")
    age = int(input("Please enter the age:"))
    animal_type = input("Please enter animal type:")

    petobject = pet.Pet(name, age, animal_type)

    print(petobject)


if __name__ == "__main__":
    main()
