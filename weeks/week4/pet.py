class Pet:
    def __init__(self, name, age, animal_type):
        self.__name = name
        self.__age = age
        self.__animal_type = animal_type

    def __str__(self):
        return f"For Pet {self.__name}, age = {self.__age}, and animal_type = {self.__animal_type}"

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_animal_type(self):
        return self.__animal_type

    def set_name(self, newname):
        self.__name = newname

    def set_age(self, newage):
        self.__age = newage

    def set_animal_type(self, newType):
        self.__animal_type = newType
