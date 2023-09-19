class Animal:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def set_age(self, age):
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def eat(self, food):
        print(f"{self.__name} is eating {food}.")

    def sleep(self, hours):
        print(f"{self.__name} sleeps for {hours} hours.")

    def __str__(self):
        return f"""Name: {self.__name}
                 \nAge: {self.__age}"""


class Dog(Animal):
    def __init__(self, name, age, breed):
        Animal.__init__(self, name, age)
        self.__breed = breed

    def set_breed(self, breed):
        self.__breed = breed

    def get_breed(self):
        return self.__breed

    def bark(self):
        print(f"{self.get_name()} is barking!")

    def __str__(self):
        return (
            "Name: "
            + self.get_name()
            + "\n"
            + "Age: "
            + str(self.get_age())
            + "\n"
            + "Breed: "
            + self.__breed
        )
